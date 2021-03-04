# Importação das bibliotecas
import cv2

# Leitura da imagem com a função imread()
image = cv2.imread('../resources/img/vermelho.jpg')
height, width, channels = image.shape

print('Largura em pixels: ', width)  # largura da imagem
print('Altura em pixels: ', height)  # altura da imagem
print('Qtde de canais: ', channels)
xi = width
xf = 0
yi = height
yf = 0
for y in range(0, height, 1):  # percorre as linhas
    for x in range(0, width, 1):  # percorre as colunas
        (b, g, r) = image[y, x]
        if (b == 0) & (g == 0) & (r > 220):
            if x < xi: xi = x
            if x > xf: xf = x
            if y < yi: yi = y
            if y > yf: yf = y

if xf - xi == yf - yi:
    print('QUADRADO')
else:
    print('RETANGULO')

print('xi= ', xi, 'xf= ', xf)
print('yi= ', yi, 'yf= ', yf)
cv2.waitKey(0)  # espera pressionar qualquer tecla
