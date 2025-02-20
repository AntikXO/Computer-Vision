import cv2 as cv

# img=cv.imread('Photos/Screenshot.png')

# cv.imshow("Img",img)
# cv.waitKey(0)

def rescaleFrame(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def resize_webcam(width,height):
    capture_webcam.set(3,width)
    capture_webcam.set(4,height)

capture=cv.VideoCapture("Videos/SaveInsta.App - 3050918822199342908.mp4")

capture_webcam=cv.VideoCapture(0)

while True:
    isTrue, frame= capture.read()

    frame_resized=rescaleFrame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Resized", frame_resized)

    # cv.imshow("Webcam",frame)

    if cv.waitKey(20) and 0xFF==ord("d"):
        break

capture.release()
cv.destroyAllWindows()
