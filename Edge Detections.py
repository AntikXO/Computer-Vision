import cv2 as cv
import numpy as np

img=cv.imread("Photos/Screenshot (179).png")
# cv.imshow("Img",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2RGB)

#Laplacian Edge Detection
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("Lap",lap)

#Sobel Edge Detection
sobel_x=cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=(cv.bitwise_or(sobel_x,sobel_y))

cv.imshow("Sobel_X", sobel_x)
cv.imshow("Sobel_y", sobel_y)
cv.imshow("Combined", combined_sobel)

#Canny Edge Detection
canny=cv.Canny(gray,150,150)
cv.imshow("Canny",canny)


cv.waitKey(0)