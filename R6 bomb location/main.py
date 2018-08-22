import os
from difflib import get_close_matches
import json
import cv2
import numpy as np
import re

from template import template
from text import text
from round import cut_match
# from Videoslicer import split_video
# from ScreenCapture import grab_screen


Map="Coastline"
TeamAzul="Element Mystic"
TeamLaranja="Millenium"

resultado="DRAW"
matchResult={}
bombsResult={}



with open("bombs.json","r") as file:
    dicjson = json.loads(file.read())

    ordered_files = sorted(os.listdir(".\\Frames"), key=lambda x: (int(re.sub('\D','',x)),x))
    lastAzul=0
    lastLaranja=0
    for i in ordered_files:
        if i!="1000.png":
            img=cv2.imread(".\\Frames\\{}".format(i))

            azul=cut_match(img,"azul")
            laranja=cut_match(img,"laranja")

            rodada=azul+laranja+1

            bomb=template("Frames\\{}".format(i),".\\templates\\atk.png")
            bomb_corrigido=get_close_matches(bomb, dicjson[Map])
            bomb_f=bomb_corrigido[0]

            lista=[bomb_f,]
            bombsResult[rodada]=lista
            lista=[]

            if (lastAzul+1)==azul and lastLaranja==laranja:
                if rodada<=6:
                    bombsResult[(rodada-1)].append(TeamAzul)
                    bombsResult[(rodada-1)].append("ATK")
                else:
                    bombsResult[(rodada-1)].append(TeamAzul)
                    bombsResult[(rodada-1)].append("DEF")

            elif lastAzul==azul and (lastLaranja+1)==laranja:
                    if rodada<=6:
                        bombsResult[(rodada-1)].append(TeamLaranja)
                        bombsResult[(rodada-1)].append("DEF")
                    else:
                        bombsResult[(rodada-1)].append(TeamLaranja)
                        bombsResult[(rodada-1)].append("ATK")

            lastAzul=azul
            lastLaranja=laranja

        elif i == "1000.png":
            img=cv2.imread(".\\Frames\\{}".format(i))
            img=img[310:395,460:815]
            result=text(img)

            if result=="MATCH DRAW" and lastAzul==4:
                bombsResult[(rodada)].append(TeamAzul)
                bombsResult[(rodada)].append("DEF")

            elif result== "MATCH DRAW" and lastLaranja==4:
                bombsResult[(rodada)].append(TeamLaranja)
                bombsResult[(rodada)].append("ATK")

            elif result!="MATCH DRAW" and lastAzul==5:
                resultado=TeamAzul
                bombsResult[(rodada)].append(TeamAzul)
                bombsResult[(rodada)].append("DEF")

            elif result!="MATCH DRAW" and lastLaranja==5:
                resultado=TeamLaranja
                bombsResult[(rodada)].append(TeamLaranja)
                bombsResult[(rodada)].append("ATK")

matchResult["Result"]=resultado
matchResult["Bombs"]=bombsResult
print(matchResult)

with open("match_{0}_{1}.json".format(TeamAzul,TeamLaranja), "w") as file:
    file.write(json.dumps(matchResult,indent=4,sort_keys=True))
