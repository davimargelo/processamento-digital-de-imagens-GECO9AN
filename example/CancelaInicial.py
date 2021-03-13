import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

try:

    from PIL import Image
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


##### Captura pela WebCam ##########
# captura = cv2.VideoCapture(0)
image = mpimg.imread('../resources/img/placa1.jpg')
# ret, frame = captura.read()
cv2.imshow("foto", image)
# captura.release()
cv2.destroyAllWindows()

# cv2.imwrite("placa1.jpg", frame)

image1 = mpimg.imread('../resources/img/placa1.jpg')
print("Altura (height): %d pixels" % (image1.shape[0]))
print("Largura (width): %d pixels" % (image1.shape[1]))
print("Canais (channels): %d" % (image1.shape[2]))

# cv2.imshow('Original', image1)
plt.figure('Original')
plt.imshow(image1)
plt.show()

print('Original')
a = (pytesseract.image_to_string(Image.open('../resources/img/placa1.jpg')))
print('Reconhecido: ', a)

print('Final sem tratatmento')
custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'
a = (pytesseract.image_to_string('../resources/img/placa1.jpg', config=custom_config))
print('Reconhecido: ', a)

##### Tratamento da imagem ######
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
thresh = thresholding(image1)
plt.figure('Thresh')
plt.imshow(image1)
plt.show()
# cv2.imshow('Thresh', image1)

print('Final com tratatmento')
custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'
a = (pytesseract.image_to_string(thresh, config=custom_config))
print('Reconhecido: ', a)
