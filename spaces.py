import cv2 as cv

img = cv.imread('Images/Cat4.jpg')
resized = cv.resize(img,(500,500))

cv.imshow('Image', resized)

# Color Spaces such as RGB, GrayScale, HSV, LAB etc

# BGR to GrayScale 
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV 
hsv = cv.cvtColor(resized, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#  BGR to L*A*B

lab = cv.cvtColor(resized, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)


# BGR Image vs RGB Image 
# OpenCV reads as BGR image which is inverse of RGB
# other library like matplot reads as RGB image 
# check for the difference

# import matplotlib.pyplot as plt 
# plt.imshow(resized)
# plt.show()

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read image in RGB format
img2 = mpimg.imread('Images/Cat4.jpg')  # or .png, .jpeg, etc.

# Display the image
plt.imshow(img2)
plt.title("Image from Matplotlib")
plt.axis('off')
plt.show()


rgb = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

# Grayscale -> BGR -> HSV --- no direct way 

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR', hsv_bgr)

#bgr_gray


cv.waitKey(0)