import cv2 as cv
import numpy as np

img=cv.imread('Photos/Screenshot.png')
cv.imshow("Img",img)

#Translation
# def translation(img,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dimensions=(img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMat,dimensions)

# translated=translation(img,-100,100)
# cv.imshow("translated",translated)

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=(img.shape[0],img.shape[1])
    dimensions=(width,height)

    if rotPoint==None:
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)

    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(img,-45)
cv.imshow("rotated",rotated)


cv.waitKey(0)