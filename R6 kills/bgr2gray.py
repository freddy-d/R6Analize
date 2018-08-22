import cv2
import numpy as np
import os




for i in os.listdir("C:\\Users\\Freddy Dratwa\\Desktop\\Python\\R6 kills\\templates\\"):
    template = cv2.imread('C:\\Users\\Freddy Dratwa\\Desktop\\Python\\R6 kills\\templates\\{}'.format(i))
    img_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("C:\\Users\\Freddy Dratwa\\Desktop\\Python\\R6 kills\\templates\\{}_gray".format(i),img_gray)
    print(i)
