import cv2 as cv

# img = cv.imread('Images/Cat.jpg')

# cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.50):
    # Works for Images, Videos and Live Feed
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Only Live Video 
    capture.set(3, width)
    capture.set(4, height)


if __name__=='__main__':
    capture = cv.VideoCapture('Videos/Dog1.mp4')

    while True:
        isTrue, frame = capture.read()
        frame_resized = rescaleFrame(frame)
        cv.imshow('Video', frame_resized)

        if cv.waitKey(20) & 0xFF ==ord('d'):
            break

    cv.waitKey(0)