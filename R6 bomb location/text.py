import numpy as np
import cv2
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

def text(img):
    ret, mask=cv2.threshold(img, 155, 255, cv2.THRESH_BINARY_INV)
    mask2=cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
    pil_img=Image.fromarray(mask2)
    result=pytesseract.image_to_string(pil_img)
    return str(result)
