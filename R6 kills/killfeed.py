import cv2
import numpy as np
import os

"""
x=943
y=182

W=336
H=41


azul
H=209
S=92
V=85

lower = np.array([80,70,90])
upper = np.array([230,250,255])

laranja
H=32
S=88
V=78

lower = np.array([0,70,90])
upper = np.array([90,230,255])
"""
def feedAzul(imagepath):
    img = cv2.imread(imagepath)
    img=img[182:223,943:1279]

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([80,70,90])
    upper = np.array([230,250,255])

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imwrite("feedAzul.png",res)
    return None
def feedLarnaja(imagepath):
    img = cv2.imread(imagepath)
    img=img[182:223,943:1279]

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = np.array([0,70,90])
    upper = np.array([90,230,255])

    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(img,img, mask= mask)
    cv2.imwrite("feedAzul.png",res)
    return None
