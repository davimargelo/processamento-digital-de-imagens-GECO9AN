import copy
import os

import cv2
from matplotlib import pyplot as plt

import algorithm
from ativ2.utils import process

try:

    from PIL import Image
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def start(name):
    print('\n')
    cv2.destroyAllWindows()
    arquivo = './resources/img/' + name
    original = cv2.imread(arquivo)  # colorida
    img = cv2.imread(arquivo, 0)  # monocromática = binária
    (alt, lar) = img.shape[:2]  # captura altura e largura
    imgT = process.thresholding(img)  # 230

    # monta os pontos
    (ponto1, ponto2, angulo) = algorithm.pegar_inclinacao(alt, lar, imgT)
    cv2.circle(imgT, (ponto1), 5, (0, 255, 0), -1)
    cv2.circle(imgT, (ponto2), 5, (0, 255, 0), -1)
    # plt.imshow(cv2.cvtColor(imgT, cv2.COLOR_BGR2RGB))
    # plt.show()

    # rotaciona
    M = cv2.getRotationMatrix2D(ponto1, angulo, 1.0)
    img_rotacionada = algorithm.girar_imagem(original, M, original.shape[1], original.shape[0])
    plt.imshow(cv2.cvtColor(img_rotacionada, cv2.COLOR_BGR2RGB))
    plt.show()

    # corta
    img_recortada = algorithm.cortar_imagem(img_rotacionada, ponto1)
    plt.imshow(cv2.cvtColor(img_recortada, cv2.COLOR_BGR2RGB))
    plt.show()

    # definir tipo de placa
    img_zoom = img_recortada[15:65, 200:380]
    img_tratada = process.thresholding(
        cv2.cvtColor(img_zoom, cv2.COLOR_BGR2GRAY)
    )
    custom_config = r'-c tessedit_char_whitelist=ABC012 --psm 6'
    tipo = (pytesseract.image_to_string(img_tratada, config=custom_config)).removesuffix('').replace('\n', '')
    print(name, tipo)
    plt.imshow(cv2.cvtColor(img_tratada, cv2.COLOR_BGR2RGB))
    plt.show()

    # comparar com gabarito
    img_gabarito = cv2.imread('./resources/img/Gabarito ' + tipo + '.jpg')

    diff = cv2.subtract(img_recortada, img_gabarito)

    img_com_diferenca = algorithm.compare(
        name,
        tipo,
        diff,
        copy.deepcopy(img_recortada),
        copy.deepcopy(img_gabarito),
        10
    )

    plt.imshow(cv2.cvtColor(img_com_diferenca, cv2.COLOR_BGR2RGB))
    plt.show()


placas_iguais = os.listdir('./resources/img/FotosPlacas')
placas_com_erro = os.listdir('./resources/img/FotosPlacasComErro')

for placa in placas_iguais:
    start('FotosPlacas/' + placa)

for placa in placas_com_erro:
    start('FotosPlacasComErro/' + placa)
