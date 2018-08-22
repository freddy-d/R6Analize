import cv2
import numpy as np
import os

def template_match(template_path, img_cut):
        match=False
        img_gray = cv2.cvtColor(img_cut, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template_path,0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
        threshold = 0.65
        loc = np.where( res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_cut, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
            match=True
        return match

def cut_match(img, cor):
    img=img.copy()
    if cor=="azul":
        img=img[30:90, 520:640]#azul
    elif cor=="laranja":
        img=img[30:90, 640:760]#laranja

    pontos=0
    for i in os.listdir(".\\templates\\round"):
        if i.endswith(".png"):
            result=template_match(".\\templates\\round\\{}".format(i),img)
            if result==True:
                pontos=int(i[0])
                break
    return pontos
