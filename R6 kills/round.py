import cv2
import numpy as np
import os

img = cv2.imread('aa.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

round=1
for i in os.listdir("C:\\Users\\Freddy Dratwa\\Desktop\\Python\\R6 kills\\templates"):
    if i.endswith(".png"):
        template = cv2.imread('C:\\Users\\Freddy Dratwa\\Desktop\\Python\\R6 kills\\templates\\{}'.format(i),0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            round+=int(i[5])
print(round)
