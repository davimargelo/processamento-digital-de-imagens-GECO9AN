import math

import cv2

# corta a imagem
from ativ2.tipos import *


def cortar_imagem(imagem, ponto1):
    pontoinicial = ponto1
    largura = 602
    altura = 295

    xi = pontoinicial[0] - largura
    xf = pontoinicial[0]
    yi = pontoinicial[1]
    yf = pontoinicial[1] + altura

    return imagem[yi:yf, xi:xf]


def girar_imagem(imgT, M, largura, altura):
    return cv2.warpAffine(imgT, M, (largura, altura))


############ descobrindo a inclinação da imagem
def pegar_inclinacao(altura, largura, imgT):
    p1 = 0
    p2 = 0
    xi = largura
    inc = 0

    # R 168, G 209, B 141 // HEX A8D18D
    for y in range(0, altura, 1):
        for x in range(0, largura, 1):
            cor = imgT[y, x]
            if cor != 255 and (p1 == 0):
                ponto1 = (x, y)
                xi = x
                p1 = 1
                if x > (largura / 2):
                    inc = 1  # para saber se a inclinação é positiva ou negativa

            if (p1 == 1) and (inc == 1) and (cor != 255) and (x < xi):
                ponto2 = (x, y)
                xi = x

            if (p1 == 1) and (inc == 0) and (cor != 255) and (x > xi):
                ponto2 = (x, y)
                xi = x

    angulo = math.atan2(ponto1[1] - ponto2[1], ponto1[0] - ponto2[0])
    if inc == 1:
        angulo = math.degrees(angulo)
    if inc == 0:
        angulo = math.degrees(angulo) + 180
        aux = ponto1
        ponto1 = ponto2
        ponto2 = aux

    print('Inclinacao = ', angulo)
    return ponto1, ponto2, angulo


def checar_placa(imagem, tipo):
    retangulo_param1 = 'RETANGULO_Y'
    retangulo_param2 = 'RETANGULO_Y'
    retangulo_param3 = 'RETANGULO_X1'
    retangulo_param4 = 'RETANGULO_X2'
    if(tipo == TIPOS.AC01.value or tipo == TIPOS.AC02.value):
        retangulo_param1 = 'RETANGULO_Y1'
        retangulo_param2 = 'RETANGULO_Y2'
        retangulo_param3 = 'RETANGULO_X'
        retangulo_param4 = 'RETANGULO_X'


    if (imagem[QUA_RET[tipo].value[retangulo_param1], QUA_RET[tipo].value[retangulo_param3]] == CORES.AZUL.value).all():
        if (imagem[QUA_RET[tipo].value[retangulo_param2], QUA_RET[tipo].value[retangulo_param4]] == CORES.AZUL.value).all():
            print('Retangulo ok')
        else:
            if tipo == TIPOS.AC01.value or tipo == TIPOS.AC02.value:
                print('Erro no retangulo, propriedade: {} nao encontrada'.format(retangulo_param2))
            else:
                print('Erro no retangulo, propriedade: {} nao encontrada'.format(retangulo_param4))
    else:
        if (imagem[QUA_RET[tipo].value[retangulo_param2], QUA_RET[tipo].value[retangulo_param4]] == CORES.AZUL.value).all():
            if tipo == TIPOS.AC01.value or tipo == TIPOS.AC02.value:
                print('Erro no retangulo, propriedade: {} nao encontrada'.format(retangulo_param1))
            else:
                print('Erro no retangulo, propriedade: {} nao encontrada'.format(retangulo_param3))
        else:
            print('Erro no retangulo, retangulo nao encontrado')


    if (imagem[QUA_RET[tipo].value['QUADRADO_Y'], QUA_RET[tipo].value['QUADRADO_X']] == CORES.AZUL.value).all():
        print('Quadrado ok')
    else:
        print('Erro no quadrado, quadrado nao encontrado')


def compare(name, tipo, difference, imagem, gabarito, color_tolerance=None):
    b, g, r = cv2.split(difference)
    t = 0

    diff_tolerance = (gabarito.shape[0] * gabarito.shape[1]) * 0.05

    if color_tolerance is not None:
        t = color_tolerance

    pixels_diferentes = 0
    for y in range(0, gabarito.shape[0], 1):
        for x in range(0, gabarito.shape[1], 1):
            if b[y, x] > t or g[y, x] > t or r[y, x] > t or b[y, x] < t * -1 or g[y, x] < t * -1 or r[y, x] < t * -1:
                imagem[y, x] = (0, 0, 255)
                pixels_diferentes = pixels_diferentes + 1

    if pixels_diferentes <= diff_tolerance:
        cv2.imwrite('results/' + tipo + '/iguais/' + name.split('/')[0] + '_' + name.split('/')[1], imagem)
        print("As imagens são semelhantes. {} pixels diferentes".format(pixels_diferentes))
    else:
        cv2.imwrite('results/' + tipo + '/diferentes/' + name.split('/')[0] + '_' + name.split('/')[1], imagem)
        print("As imagens são diferentes. {} pixels diferentes".format(pixels_diferentes))
        checar_placa(imagem, tipo)

    return imagem
