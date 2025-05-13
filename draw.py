import cv2 as cv
import numpy as np 

blank = np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank',blank)

# 1. Paint the image a certain color 
# blank[:] = 0,255,0

# blank[100:200, 200:400] = 0,0,255

# cv.imshow('Red', blank)

# 2. Draw a Rectangle 
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
# OR thickness = -1 -> same result as cv.FILLED

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,255,0), thickness=-1)

cv.imshow('Rectangle',blank)

# 3. Draw a circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)

# 4. Draw a Line 
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow('Line', blank)


# 5. Write text on an Image 
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', blank)

# img = cv.imread('Images/Cat4.jpg')
# cv.imshow('Cat',img)

cv.waitKey(0)