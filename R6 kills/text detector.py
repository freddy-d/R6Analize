import pytesseract
from PIL import Image
import numpy as np
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def text(imagepath):
    img = cv2.imread(imagepath)
    img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.erode(img, kernel, iterations=13)
    img = cv2.dilate(img, kernel, iterations=13)
    ret, mask = cv2.threshold(img2gray, 155, 255, cv2.THRESH_BINARY_INV)
    cv2.imwrite("tessa.png",mask)


    img=Image.open('tessa.png')
    result =pytesseract.image_to_string(img)
    with open("killfeed.txt", "a") as file:
        file.write(result)
        file.write("\n")
    return None
