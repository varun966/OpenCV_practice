import cv2 as cv

img = cv.imread('Images/Cat4.jpg')
resized = cv.resize(img, (500,500))
cv.imshow('Image', resized)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Simple Thresholding 
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

# 150 - threshold value
# 255 - value to set if value >=150
# returns: thresh -> thresholded image and threshold -> value that we passed i.e 150
cv.imshow('Simple Thresholded', thresh)

# Simple Threshold inverse 

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded INV', thresh)


# Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, maxValue=255, adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv.THRESH_BINARY,
                                     blockSize=11, C=3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)



cv.waitKey(0)