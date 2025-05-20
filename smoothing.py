import cv2 as cv 
import numpy as np

img = cv.imread('Images/Cat4.jpg')
resized = cv.resize(img, (500,500))
cv.imshow('Image', resized)

# Averaging Blur
average = cv.blur(resized, (3,3))
cv.imshow('Average', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(resized,(3,3), 0) # 0 -> standard deviation in x direction --> SigmaX
cv.imshow('Gaussian', gaussian)

# Median Blurring 
median = cv.medianBlur(resized, 3) # creates a tuple of 3,3 based on the given value
cv.imshow('Median', median)

# Bilateral blurring -> retains edges
bilateral = cv.bilateralFilter(resized, 10, 15, 50) # sigmacolor ? sigmaspace ?
cv.imshow('bilateral', bilateral)

# Box 
box = cv.boxFilter(resized, -1, (3,3), normalize=True)
cv.imshow('Box Filter', box )

# custom Kernel blurring
kernel = np.ones((3,3), np.float32) / (3 * 3)
custom = cv.filter2D(resized, -1, kernel)
cv.imshow('Custom', custom)



cv.waitKey(0)