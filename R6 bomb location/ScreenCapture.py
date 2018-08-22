import numpy as np
import cv2
import os
import win32gui, win32ui, win32con, win32api
import time

from text import text

def grab_screen(region=None):

    hwin = win32gui.GetDesktopWindow()

    if region:
            left,top,x2,y2 = region
            width = x2 - left + 1
            height = y2 - top + 1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return img


try:
    if not os.path.exists("FramesLive"):
        os.makedirs("FramesLive")
    for i in os.listdir("./FramesLive"):
        j=i[:-4]
        os.remove("FramesLive\\"+i)
except:
    None


stop=cv2.imread("stop.jpg")
stop=cv2.resize(stop,(0,0), fx=0.20, fy=0.20)

contador=0
while(True):
    # frame=cv2.resize(grab_screen(region=(0,0,3840,2160)),(0,0), fx=0.125, fy=0.125)
    frame=grab_screen(region=(0,0,3840,2160))

    frame_copy=frame.copy()
    frame_copy=frame_copy[350:490,290:1150]
    phase=text(frame_copy)

    frame_copy2=frame.copy()
    frame_copy2=frame_copy2[130:245,1825:2035]
    timer=text(frame_copy2)
    # print(timer)

    if phase=="6TH PICK PHASE" and timer=="0:00":
        cv2.imwrite("./FramesLive/{}.png".format(str(contador)), frame)
        contador+=1
        # time.sleep(30)

    # frame_copy2=frame.copy()
    # frame_copy2=frame_copy2[380:450,565:715]
    # end=text(frame_copy2)
    # if end=="TDM - BOMB\nCUSTOM GAME":
    #     cv2.imwrite("./Frames/1000.png", frame)

    # frame2=cv2.resize(frame_copy2,(0,0), fx=0.25, fy=0.25)
    cv2.imshow("Control",stop)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
