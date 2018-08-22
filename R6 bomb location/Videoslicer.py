import numpy as np
import cv2
import os
from text import text


def split_video(videoName):
    cap = cv2.VideoCapture(videoName)

    try:
        if not os.path.exists("Frames"):
            os.makedirs("Frames")
        for i in os.listdir("./Frames"):
            j=i[:-4]
            os.remove("Frames\\"+i)
    except:
        None

    currentFrame=0
    length=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    contador=0
    while(currentFrame<=length):
        ret, frame = cap.read()
        cap.set(cv2.CAP_PROP_POS_FRAMES,currentFrame)

        frame_copy=frame.copy()
        frame_copy=frame_copy[100:180,80:350]
        phase=text(frame_copy)

        frame_copy2=frame.copy()
        frame_copy2=frame_copy2[380:450,565:715]
        end=text(frame_copy2)

        if phase=="6TH PICK PHASE":
            cv2.imwrite("./Frames/{}.png".format(str(contador)), frame)
            currentFrame+=500
            contador+=1
        if end=="TDM - BOMB\nCUSTOM GAME":
            cv2.imwrite("./Frames/1000.png", frame)
            currentFrame+=10

        if currentFrame<=95*(length/100):
            currentFrame+=200
        else:
            currentFrame+=10

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # print(end)

    for i in os.listdir("./Frames"):
        j=i[:-4]
        if int(j)%2!=0:
            os.remove("Frames\\"+i)

    cap.release()
    cv2.destroyAllWindows()
    return None
