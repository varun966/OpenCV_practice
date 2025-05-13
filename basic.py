import cv2 as cv
from rescale import rescaleFrame

img = cv.imread('Images/Cat4.jpg')
img = rescaleFrame(img)

cv.imshow('Cat', img)

# COnverting to GrayScale 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur an Image

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade 
canny = cv.Canny(img, 125, 175)
# canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Dilating the Image - we will dilate the canny edge features 

dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding - opposite of dilation 

eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded',eroded)

# Resize
resized = cv.resize(img, (500,500)) # Ignores the aspect ration
# resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA) useful when you are shrinking an image that is smaller than the
# original dimension
# For enlarging, we use interpolation=cv.INTER_LINEAR or cv.INTER_CUBIC, cubic is slower but results in much higher quality
cv.imshow('Resized', resized)


# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)