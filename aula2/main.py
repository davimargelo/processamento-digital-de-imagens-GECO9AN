import cv2

imagem = cv2.imread('../resources/img/entrada.jpg')
(b, g, r) = imagem[0, 0]  # veja que a ordem BGR e não RGB
print('O pixel (0, 0) tem as seguintes cores:')
print('Vermelho:', r, 'Verde:', g, 'Azul:', b)
