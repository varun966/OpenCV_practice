import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Images/Cat4.jpg')
resized = cv.resize(img,(500,500))

cv.imshow('Image', resized)

# GRayScale
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Grayscale-Histogram
gray_hist = cv.calcHist(images=[gray], channels=[0], mask=None, histSize=[256], ranges=[0,255] )


plt.figure('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()


# We can use masking to get a histogram for a particular region


# Color Histogram 
plt.figure()
plt.title('Color Histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    color_hist = cv.calcHist(images=[resized], channels=[i], mask=None, histSize=[256], ranges=[0,256])
    plt.plot(color_hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)