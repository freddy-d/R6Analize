import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('example.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while(currentFrame<=length):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    if currentFrame%3000==0:
        name = './data/second' + str(int((currentFrame/30))) + '.png'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
