import cv2 as cv
import numpy as np 


img = cv.imread('Images/Cat4.jpg')
resized = cv.resize(img, (500,500))
cv.imshow('Image', resized)
print(resized.shape)

# should always be the same size as of the image 
blank = np.zeros(resized.shape[:2], dtype='uint8')

mask = cv.circle(blank, (resized.shape[1]//2, resized.shape[0]//2-70), 150, 255, thickness=-1)

masked_img = cv.bitwise_and(resized, resized, mask = mask)
cv.imshow('Masked Image', masked_img)


cv.waitKey(0)