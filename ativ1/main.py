import cv2
import matplotlib.image as mpimg
from matplotlib import pyplot as plt
import TableIT
import process

try:

    from PIL import Image
except ImportError:
    import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
table = [
    ['Texto', 'Altura (pixels)', 'Largura (pixels)']
]
placas_permitidas = ['ABC1B34', 'EWK-7037']
print('Lista de placas liberadas: {}'.format(placas_permitidas))

def buildTable(image, text):
    index = len(table)
    table.append([])
    table[index].append(text)
    table[index].append(str(image.shape[0]))
    table[index].append(str(image.shape[1]))


def filter(placa):
    if placa in placas_permitidas:
        print('Placa {} liberada'.format(placa))
    else:
        print('Placa {} não liberada'.format(placa))


def read1():
    placa1 = mpimg.imread('resources/img/placa1.jpg')
    placa1 = cv2.cvtColor(placa1, cv2.COLOR_BGR2GRAY)
    processed_placa1 = process.thresholding(placa1)

    custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'
    a = (pytesseract.image_to_string(processed_placa1, config=custom_config)).removesuffix('').replace('\n', '')

    filter(a)
    buildTable(placa1, a)

    plt.imshow(cv2.cvtColor(processed_placa1, cv2.COLOR_BGR2RGB))
    plt.show()


def read2():
    placa2 = mpimg.imread('resources/img/placa2.jpg')
    placa2 = cv2.cvtColor(placa2, cv2.COLOR_BGR2GRAY)
    processed_placa2 = process.dilate(placa2)

    custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'
    a = (pytesseract.image_to_string(processed_placa2, config=custom_config)).removesuffix('').replace('\n', '')

    filter(a)
    buildTable(placa2, a)

    plt.imshow(cv2.cvtColor(processed_placa2, cv2.COLOR_BGR2RGB))
    plt.show()


def read3():
    placa3 = mpimg.imread('resources/img/placa3.jpg')
    placa3 = cv2.cvtColor(placa3, cv2.COLOR_BGR2GRAY)
    processed_placa3 = process.thresholding(placa3)

    custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 6'
    a = (pytesseract.image_to_string(processed_placa3, config=custom_config)).removesuffix('').replace('\n', '')

    filter(a)
    buildTable(placa3, a)

    plt.imshow(cv2.cvtColor(processed_placa3, cv2.COLOR_BGR2RGB))
    plt.show()


def readNova():
    placa4 = mpimg.imread('resources/img/placa_nova.jpg')
    placa4 = cv2.cvtColor(placa4, cv2.COLOR_BGR2GRAY)
    processed_placa4 = process.erode(placa4)

    custom_config = r'-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 --psm 6'
    a = (pytesseract.image_to_string(processed_placa4, config=custom_config)).removesuffix('').replace('\n', '')

    filter(a)
    buildTable(placa4, a)

    plt.imshow(cv2.cvtColor(processed_placa4, cv2.COLOR_BGR2RGB))
    plt.show()


read1()
read2()
read3()
readNova()

TableIT.printTable(table)
