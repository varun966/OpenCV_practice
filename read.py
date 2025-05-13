import cv2 as cv

# img = cv.imread('Images/Cat4.jpg')

# cv.imshow('Cat', img)

# Reading Videos
capture = cv.VideoCapture('Videos/Dog1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# cv.waitKey(0)