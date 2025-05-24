import cv2 as cv
import numpy as np

flag = False 
ix = -1
iy = -1

img_temp = cv.imread('Images/Cat4.jpg')

img = cv.resize(img_temp,(800,800))
#org_copy = img.copy()

def crop(event, x, y, flags, params):
    
    global flag, ix, iy

    if event == 1:
        flag = True 
        ix = x 
        iy = y

    elif event == 0:
        if flag:
            temp = img.copy()  # Always draw on a clean copy
            cv.rectangle(temp, (ix, iy), (x, y), (0, 255, 0), 1)
            cv.imshow('Image', temp)  # Show the temporary image with the live rectangle

    elif event == 4:
        flag = False
        #cv.rectangle(img, pt1=(ix, iy), pt2=(x, y), thickness=1, color=(0,0,0))
        # tst = img[iy:y,ix:x]
        # cv.imshow('crop', tst)
        
        # Ensure coordinates are in top-left to bottom-right order
        x1, x2 = sorted([ix, x])
        y1, y2 = sorted([iy, y])
        crop_img = img[y1:y2, x1:x2]
        cv.imshow('Cropped', crop_img)

    


cv.namedWindow(winname='Image')
cv.setMouseCallback('Image', crop)



while True:

    cv.imshow('Image', img)

    if cv.waitKey(1) & 0xFF == ord('x'):
        break



cv.destroyAllWindows()



