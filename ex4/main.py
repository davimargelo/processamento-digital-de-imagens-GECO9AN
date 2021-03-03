import cv2

image = cv2.imread('../resources/img/entrada.jpg')
height, width, channels = image.shape

# 1
# Moldura superior
image[0:10, :] = (0, 0, 0)

# Moldura esquerda
image[:, 0:10] = (0, 0, 0)

# Moldura direita
image[:, width - 10:width] = (0, 0, 0)

# Moldura inferior
image[height - 10:height, :] = (0, 0, 0)

# 2
cv2.putText(image, "Davi Margelo", (150, height - 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0))

# 3
for x in range(0, width, 1):  # percorre as linhas
    for y in range(0, height, 1):  # percorre as colunas
        (b, g, r) = image[y, x]
        if (b > 200) & (g > 200) & (r > 200):
            image[y, x] = (0, 200, 0)
        if (b < 20) & (g < 20) & (r < 20):
            image[y, x] = (0, 50, 0)

cv2.imshow("Verde", image)
cv2.imwrite("results/saida_ex_4.jpg", image)
cv2.waitKey(0)

# 4
image = cv2.imread('../resources/img/cores.jpg')
height, width, channels = image.shape

for x in range(0, width, 1):  # percorre as linhas
    for y in range(0, height, 1):  # percorre as colunas
        (b, g, r) = image[y, x]
        image[y, x] = ((255 - b), (255 - g), (255 - r))

cv2.imshow("Cor invertida", image)
cv2.imwrite("results/saida_ex_4_cor_invertida.jpg", image)
cv2.waitKey(0)
