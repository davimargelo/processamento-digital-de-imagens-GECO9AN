import cv2

imagem = cv2.imread('../resources/img/entrada.jpg')

for b in range(0, 255, 1):  # percorre as linhas
    for g in range(0, 255, 10):  # percorre as colunas
        for r in range(0, 255, 10):  # percorre as colunas
            imagem[b, int(25 * g / 10 + r / 10)] = (b, g, r)

cv2.imshow("Result", imagem)
cv2.waitKey(0)  # espera pressionar qualquer tecla
