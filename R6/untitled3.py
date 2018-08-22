# -*- coding: utf-8 -*-
"""
Created on Mon May 21 00:31:01 2018

@author: Freddy Dratwa
"""

import cv2
import numpy as np

opATC=["lion","finka","dokkaebi","zofia","ying","jackal","hibana","capitao","blackbeard","buck","sledge","thatcher",
       "ash","thermite","montagne","twitch","blitz","iq","fuze","glaz"]

opDEF=["vigil","ela","lesion","mira","echo","caveira","valkyrie","frost","mute","smoke",
       "castle","pulse","doc","rook","jager","bandit","tachanka","kapkan"]

ops=["lion","finka","vigil","dokkaebi","zofia","ela","ying","lesion","mira","jackal","hibana","echo","caveira"
     ,"capitao","blackbeard","valkyrie","buck","frost","mute","sledge","smoke","thatcher",
     "ash","castle","pulse","thermite",
     "montagne","twitch","doc","rook","jager","bandit","blitz","iq","fuze","glaz","tachanka","kapkan"]

#def comparar(photo):
operador=""
image= cv2.imread("1.png")
img_rgb=image#[150:250,1200:1300]
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

#for i in ops:
template=cv2.imread("C:/Users/Freddy Dratwa/Desktop/R6/Logos/bandit.png", 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
cv2.imwrite("C:/Users/Freddy Dratwa/Desktop/detetcted.png", img_rgb) 
       
     
       
#print(operador)      
#cv2.imwrite("C:/Users/Freddy Dratwa/Desktop/a344.png", image1) 