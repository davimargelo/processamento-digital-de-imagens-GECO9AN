# Importação das bibliotecas
import cv2

imagem = cv2.imread('../resources/img/cores.jpg')
(b, g, r) = imagem[100, 100]  # veja que a ordem BGR e não RGB
print('O pixel (100, 100) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

(b, g, r) = imagem[200, 100]  # veja que a ordem BGR e não RGB
print('O pixel (200, 100) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

(b, g, r) = imagem[300, 100]  # veja que a ordem BGR e não RGB
print('O pixel (300, 100) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

(b, g, r) = imagem[400, 100]  # veja que a ordem BGR e não RGB
print('O pixel (400, 100) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

(b, g, r) = imagem[500, 100]  # veja que a ordem BGR e não RGB
print('O pixel (500, 100) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)

