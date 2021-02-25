import cv2

imagem = cv2.imread('../resources/img/entrada.jpg')

for x in range(0, imagem.shape[1], 20): #percorre as linhas
    for y in range(0, imagem.shape[0], 20): #percorre as colunas
        for ax in range (0,5,1):
            for ay in range (0,5,1):
                imagem[y+ay, x+ax] = (0,255,0)

cv2.imshow("Nome da janela", imagem)
cv2.waitKey(0)  # espera pressionar qualquer tecla
