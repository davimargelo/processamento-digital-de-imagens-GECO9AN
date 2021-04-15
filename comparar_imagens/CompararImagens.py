import cv2
from utils import process
import copy
import time;

original = cv2.imread("../resources/img/Modelo.jpg")
duplicate = cv2.imread("../resources/img/Recorte.jpg")

def compare(difference, original, duplicate, tolerance=None):
    b, g, r = cv2.split(difference)
    t = 0

    if tolerance is not None:
        t = tolerance

    for y in range(0, original.shape[0], 1):
        for x in range(0, original.shape[1], 1):
            if b[y, x] > t or g[y, x] > t or r[y, x] > t:
                duplicate[y, x] = (0, 0, 255)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("The images are completely Equal")

    if cv2.countNonZero(b) != 0 or cv2.countNonZero(g) != 0 or cv2.countNonZero(r) != 0:
        print("The images are not completely Equal")
    cv2.imshow("Original " + str(time.time()), original)
    cv2.imshow("Duplicate " + str(time.time()), duplicate)

# 1) Check if 2 images are equals
if original.shape == duplicate.shape:
    print("The images have same size and channels")

# com as imagens sem tratamento, faz a comparação
compare(cv2.subtract(original, duplicate), copy.deepcopy(original), copy.deepcopy(duplicate), 30)

# com as imagens preta e brancas faz a comparação
original_black = process.thresholding(cv2.cvtColor(original, cv2.COLOR_BGR2GRAY))
duplicate_black = process.thresholding(cv2.cvtColor(duplicate, cv2.COLOR_BGR2GRAY))
difference_black = cv2.subtract(original_black, duplicate_black)
compare(cv2.cvtColor(difference_black, cv2.COLOR_GRAY2BGR), original_black, cv2.cvtColor(duplicate_black, cv2.COLOR_GRAY2BGR))

# com as imagens cinzas faz a comparação
original_gray = process.erode(cv2.cvtColor(original, cv2.COLOR_BGR2GRAY))
duplicate_gray = process.erode(cv2.cvtColor(duplicate, cv2.COLOR_BGR2GRAY))
difference_gray = cv2.subtract(cv2.cvtColor(original_gray, cv2.COLOR_GRAY2BGR), cv2.cvtColor(duplicate_gray, cv2.COLOR_GRAY2BGR))
compare(difference_gray, original_gray, cv2.cvtColor(duplicate_gray, cv2.COLOR_GRAY2BGR), 15)

# original_gray=process.erode(cv2.cvtColor(original, cv2.COLOR_BGR2GRAY))

# cv2.imshow("Preta e branca", original_black)
# cv2.imshow("Tons de cinza", original_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
