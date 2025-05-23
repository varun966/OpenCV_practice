import cv2 as cv
import numpy as np

drawing = False
ix = -1 
iy = -1



# Event Listener
def draw(event, x, y, flags, params):

    # if event == 0:
    #     print('Mouse Moved')
    # elif event==1:
    #     print("Mouse Clicked/ Down Pressed ")
    # elif event == 4:
    #     print('Mouse Unclicked/Released')

    global drawing, ix, iy   # as we are changing outside value inside the function

    if event == 1:
        drawing = True 
        ix = x
        iy = y 

    elif event == 0:
        if drawing == True:
            cv.rectangle(img, pt1=(ix, iy), pt2=(x,y), color=(0,255,0), thickness=-1)

    elif event == 4:
        drawing=False
        cv.rectangle(img, pt1=(ix, iy), pt2=(x,y), color=(0,255,0), thickness=-1)

         

cv.namedWindow(winname="blank")
cv.setMouseCallback("blank", draw)


# Read an Image 
img = np.zeros((512,512,3))

while True:

    cv.imshow('blank', img) 

    if cv.waitKey(1) & 0xFF == ord('x'):
        break

cv.destroyAllWindows()