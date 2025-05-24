import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter.fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:

    ret, frame = cap.read()
    out.write(frame)

    cv.imshow('WebCam', frame)

    if cv.waitKey(1) & 0xFF == ord('x'):
        break

out.release()
cv.destroyAllWindows()