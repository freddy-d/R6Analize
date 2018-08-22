import cv2
import numpy as np
import os

def black(imagepath):
    img = cv2.imread(imagepath)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,10,255,cv2.THRESH_BINARY)
    im2,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x,y,w,h = cv2.boundingRect(cnt)
    crop = img[y:y+h,x:x+w]
    cv2.imwrite("crop.png",crop)
    return None

cv2.imshow('crop',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
