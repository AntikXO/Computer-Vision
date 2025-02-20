import cv2 as cv
import numpy as np

blank=np.zeros((600,600,3),dtype="uint8")
blank[:]=173,248,2

# #Draw a rectangle
# cv.rectangle(blank,(0,0),(200,300),(89,255,90),thickness=-1)
# cv.imshow("Rectangle",blank)

# #Draw a circle
# cv.circle(blank,(300,300),50,(0,0,255),-1)
# cv.imshow("Circle",blank)

# #Draw a line
# cv.line(blank,(300,555),(200,300),(255,255,250),thickness=9)
# cv.imshow("Line",blank)

#Write text
cv.putText(blank,"brat",(230,300),cv.FONT_HERSHEY_DUPLEX,2.0,(0,0,0),2)
cv.imshow("brat",blank)

cv.waitKey(0)