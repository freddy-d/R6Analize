# -*- coding: utf-8 -*-
"""
Created on Mon May 21 13:28:10 2018

@author: Freddy Dratwa
"""

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt




img_rgb = cv.imread('0.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)



template = cv.imread("C:/Users/Freddy Dratwa/Desktop/R6/Logos/bandit.png",0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite('res.png',img_rgb)
cv.imwrite('template.png',img_rgb)



