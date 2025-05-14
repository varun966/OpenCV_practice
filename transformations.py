import cv2 as cv
import numpy as np

img = cv.imread('Images/Cat4.jpg')
resized = cv.resize(img, (500,500))

cv.imshow('Cat',resized)

# Translation 
# Shifting the images along the x and y axis
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x = left x= right
# -y = up  y = down

translated = translate(resized, -100, 100)
cv.imshow('Translated', translated)


# Rotation
# Open CV allows to rotate the image from any point....not necessarily the center of the image
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(resized, 45)
cv.imshow('Rotoated', rotated)

# Flipping 
flip = cv.flip(resized, -1)
cv.imshow('Flipped', flip)

# 0 - flip the image along x -axis  - vertical flip
# 1 - flip the image along y - axis  - horizontal flip
# -1 - flip the image along both the axes

cv.waitKey(0)