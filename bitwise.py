import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)  # sincl=e binary image only one color 255(white), 
                                                                     #thickness -1 that is filled
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle',circle)

# Finds the intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('AND', bitwise_and)

# Finds the intersecting + non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('OR', bitwise_or)

# Finds the non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR', bitwise_xor)

# bitwise not - just inverts binary color 
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('rectangle_not', bitwise_not) 

cv.waitKey(0)