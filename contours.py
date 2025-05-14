import cv2 as cv
import numpy as np

img = cv.imread('Images/Cat4.jpg')
resized = cv.resize(img, (500,500))

cv.imshow('Cat', resized)

# Converting to GrayScale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)


blur = cv.GaussianBlur(gray,(5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Another way of doing it

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

countours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Blank Image 

blank = np.zeros(resized.shape, dtype='uint8')

# Draw contours on blank image
cv.drawContours(blank, countours, -1, (0,0,255), thickness=1)
cv.imshow('Drawn Contours', blank)


cv.waitKey(0)