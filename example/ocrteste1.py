import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg

try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# noise removal
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


# dilation
def dilate(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.dilate(image, kernel, iterations=1)


# erosion
def erode(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.erode(image, kernel, iterations=1)


# opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5, 5), np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)


# skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated


# template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


#########################

image1 = mpimg.imread('../resources/img/placa.jpg')

gray = get_grayscale(image1)
thresh = thresholding(gray)
opening = opening(gray)
canny = canny(gray)

plt.imshow(image1)
plt.show()
plt.imshow(gray)
plt.show()
plt.imshow(thresh)
plt.show()
plt.imshow(opening)
plt.show()
plt.imshow(canny)
plt.show()
# cv2.imshow("Original", image1)
# cv2.imshow("Gray", gray)
# cv2.imshow("thresh", thresh)
# cv2.imshow("opening", opening)
# cv2.imshow("canny", canny)

print("Altura (height): %d pixels" % (image1.shape[0]))
print("Largura (width): %d pixels" % (image1.shape[1]))
print("Canais (channels): %d" % (image1.shape[2]))

# Salva a imagem
cv2.imwrite("results/image2.jpg", gray)
print(pytesseract.image_to_string(Image.open('results/image2.jpg')))
