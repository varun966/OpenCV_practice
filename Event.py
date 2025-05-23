import cv2 as cv
import numpy as np

# Event Listener
def draw(event, x, y, flags, params):

    # if event == 0:
    #     print('Mouse Moved')
    # elif event==1:
    #     print("Mouse Clicked")
    # elif event == 4:
    #     print('Mouse Unclicked/Released')

    if event == 1:
        cv.circle(img, center=(x,y), radius=50, color=(0,0,255), thickness=-1) 

cv.namedWindow(winname="blank")
cv.setMouseCallback("blank", draw)


# Read an Image 
img = np.zeros((512,512,3))

while True:

    cv.imshow('blank', img) 

    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cv.destroyAllWindows()