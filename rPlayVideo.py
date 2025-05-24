import cv2 as cv 
import numpy as np
import time 

cap = cv.VideoCapture('output.avi')



while True:

    ret, frame = cap.read()

    time.sleep(1/20)
    cv.imshow('WebCam', frame)

    if cv.waitKey(1) & 0xFF == ord('x'):
        break


cv.destroyAllWindows()