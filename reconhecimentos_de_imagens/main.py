# Importação das bibliotecas
import cv2
import numpy
from matplotlib import pyplot as plt

# Leitura da imagem com a função imread()
image = cv2.imread('../resources/img/Direita.jpg') if numpy.random.randint(0, 10) > 5 else cv2.imread('../resources/img/Esquerda.jpg')
print('Largura em pixels: ', image.shape[1])  # largura da imagem
print('Altura em pixels: ', image.shape[0])  # altura da imagem
print('Qtde de canais: ', image.shape[2])
xi = image.shape[1]
xf = 0

for y in range(0, image.shape[0], 1):  # percorre as linhas
    for x in range(0, image.shape[1], 1):  # percorre as colunas
        (b, g, r) = image[y, x]
        if (b == 0) & (g == 0) & (r == 0):
            if x < xi: xi = x
            if x > xf: xf = x
            if x < xf: xm = x
print('xi= ', xi, 'xf= ', xf, 'xm= ', xm)
if xm < (xi + xf) / 2: text = 'DIREITA'
if xm > (xi + xf) / 2: text = 'ESQUERDA'
print(text)
# cv2.imshow(text, image)
plt.figure('Title')
plt.imshow(image)
plt.show()
cv2.waitKey(0)  # espera pressionar qualquer tecla
