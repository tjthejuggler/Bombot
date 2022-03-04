from ast import Not
from distutils.errors import DistutilsArgError
import cv2 as cv
import numpy as np

#device =graph.get_input_devices().index("Logitech BRIO")
#videocapture = cv.VideoCapture(device)
videocapture = cv.VideoCapture(cv.CAP_DSHOW)
#videocapture = cv.VideoCapture(0 + cv.CAP_DSHOW)
#videocapture = cv.VideoCapture(0)
prevcircle = None
#0 is internal cam
#1 errors
#-1 doesn't work at all
#2 black screen but might work

dist = lambda x1, y1, x2, y2: (x1-x2)**2 + (y1-y2)**2

while True:
    print('aaa')
    ret, frame = videocapture.read()
    if not ret: break

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(grayFrame, (17,17),0)
#first two integers must be odd.  the larger the number the more blurred it is.
    #cv.imshow('blurFrame', blurFrame)

    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=10, maxRadius=500)
#third variable is distance between circle
#4th variable is minimum distance between 2 circles found
#param1 is sensitivity.  Too high will not be enough circle and too low will be too many circles
#param2 sets the number of edgepoints needed to declare a circle
#minRadius is minimum size of a circle that can be detected.  Webcam distance matters
#maxRadius is max size of a circle

    if circles is not None:
        circles=np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]:
            print(len(circles[0, :]))
            if chosen is None: chosen = i
            if prevcircle is not None:
                if dist(chosen[0],chosen[1],prevcircle[0],prevcircle[1]) <= dist(i[0],i[1],prevcircle[0],prevcircle[1]):
                    chosen = i
        
        cv.circle(frame, (chosen[0],chosen[1]), 1, (0,100,100), 3)
        #cv.circle(frame, (chosen[0],chosen[1]), chosen[2], (255,0,255),3)
        prevcircle = chosen

    cv.imshow("circles", frame)

    if cv.waitKey(30) & 0xFF == ord('q'): break

videocapture.release()
cv.destroyAllWindows()