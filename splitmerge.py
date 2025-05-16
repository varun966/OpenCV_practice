import cv2 as cv
import numpy as np 

img = cv.imread('Images/Cat4.jpg')
resized = cv.resize(img, (500,500))

cv.imshow('Image', resized)

b,g,r = cv.split(resized)
cv.imshow('Blue', b) # but shows these as a GrayScale (intensities)
cv.imshow('Read', r)
cv.imshow('Green',g)

print(resized.shape)
print(r.shape)
print(g.shape)
print(b.shape)


merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)

# Showing split colors properly 

blank = np.zeros(resized.shape[:2], dtype='uint8')

br,gr,rr = cv.split(resized)
blue = cv.merge([br,blank,blank])
green = cv.merge([blank,gr,blank])
red = cv.merge([blank,blank,rr])

cv.imshow('ARed',red)
cv.imshow('ABlue',blue)
cv.imshow('AGreen',green)

cv.waitKey(0)