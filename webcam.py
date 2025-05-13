# import cv2 as cv

# # 0 = default webcam (you can try 1, 2... for external webcams)
# capture = cv.VideoCapture(0)

# while True:
#     isTrue, frame = capture.read()

#     if not isTrue:
#         print("Failed to grab frame")
#         break

#     cv.imshow('Webcam', frame)

#     # Press 'q' to quit
#     if cv.waitKey(1) & 0xFF == ord('q'):
#         break

# capture.release()
# cv.destroyAllWindows()


import cv2 as cv
from screeninfo import get_monitors

# Get the screen resolution of the primary monitor
monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height

# Open the webcam
capture = cv.VideoCapture(0)

# Create a named window and set it to be resizable
cv.namedWindow("Webcam", cv.WINDOW_NORMAL)

# Set window size to a percentage of the screen size (e.g., 80% of screen size)
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)

cv.resizeWindow("Webcam", window_width, window_height)

while True:
    isTrue, frame = capture.read()

    if not isTrue:
        print("Failed to grab frame")
        break

    # Resize the frame to fit the window (optional, but keeps it proportional)
    frame_resized = cv.resize(frame, (window_width, window_height))

    cv.imshow('Webcam', frame_resized)

    # Press 'q' to quit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
