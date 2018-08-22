import numpy as np
import cv2
import os
import re
from round import cut_match
from text import text


# for j in os.listdir(".\\data"):
#     img=cv2.imread(".\\data\\{}".format(j))
#     azulpontos=cut_match(img,"azul")
#     laranjapontos=cut_match(img,"laranja")
#     rodada=azulpontos+laranjapontos+1
#     print(rodada)

# print(os.listdir(".\\data"))
# j=(os.listdir(".\\data"))
# ordered_files = sorted(j, key=lambda x: (int(re.sub('\D','',x)),x))
# print(ordered_files)

# rodada=2
# bombsResult={ 1: ["B Laundry Room\nB Suply Room"], 2: ["2F Kids Dorms\n2F Dorms Main Hall"] }
# bombsResult[(rodada-1)].append("penta")
# print(bombsResult)

# img=cv2.imread("final.jpg")
# img=img[385:450,570:710]
# phase=text(img)
# cv2.imshow("img",img)
# cv2.waitKey(0)
# print(phase)
# cv2.destroyAllWindows()
#
#
#
# print("TDM - BOMB\nCUSTOM GAME")



# 
# img=cv2.imread(".\\Frames\\1000.png")
# img=img[310:395,460:815]
# result=text(img)
# cv2.imshow("img", img)
# print(result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
