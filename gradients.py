import cv2 as cv
import numpy as np


img = cv.imread('Images/Cat4.jpg')
resized = cv.resize(img, (500,500))
cv.imshow('Image', resized)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Grayed', gray)


# Laplacian

lap = cv.Laplacian(gray, ddepth=cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)

# Sobel 
sobelx = cv.Sobel(gray, ddepth=cv.CV_64F, dx=1, dy=0)
sobely = cv.Sobel(gray, ddepth=cv.CV_64F, dx=0, dy=1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('SobelX', sobelx)
cv.imshow('SobelY', sobely)
cv.imshow('Combined Sobel', combined_sobel)

cv.waitKey(0)