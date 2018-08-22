import numpy as np
import cv2
from text import text

def template(img_path, template_path):
    img=cv2.imread(img_path)
    img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template=cv2.imread(template_path,0)

    w, h=template.shape[::-1]
    res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold=0.8
    loc=np.where(res>=threshold)

    for pt in zip(*loc[::-1]):

        if pt[0]>700: #azul defesa// laranja ataque
            img=img[385:435, 530:750]
        else: #azul ataque// laranja defesa
            img=img[635:685, 530:750]
        break

    bomb=text(img)
    return bomb
