# -*- coding: utf-8 -*-
"""
Created on Mon May 21 09:24:16 2018

@author: Freddy Dratwa
"""

import cv2
import numpy as np

img_rgb = cv2.imread('2.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

logo=cv2.imread("C:/Users/Freddy Dratwa/Desktop/R6/Logos/bandit.png",0)
template = cv2.resize(logo,(50,50))
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)


cv2.imwrite("C:/Users/Freddy Dratwa/Desktop/detetcted.jpg", img_rgb)
cv2.imwrite("C:/Users/Freddy Dratwa/Desktop/template.jpg", template)
cv2.imwrite("C:/Users/Freddy Dratwa/Desktop/res.jpg", res)