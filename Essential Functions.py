import cv2 as cv

img=cv.imread('Photos/Screenshot (179).png')
cv.imshow("main",img)

# #Converting to grayscale
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

# #Blur
# blur=cv.GaussianBlur(img, (11,11), cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)

# #Edge Cascade
# canny=cv.Canny(img,155,100)
# cv.imshow("canny",canny)

# #Dilating an image
# dilated=cv.dilate(canny,(11,11),iterations=3)
# cv.imshow("dilated",dilated)

# #Eroding
# eroded=cv.erode(dilated,(11,11),iterations=3)
# cv.imshow("eroded",eroded)

#Resizing
resized=cv.resize(img,(400,400),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",resized)

#Cropping
cropped=img[200:700]
cv.imshow("Cropped",cropped)

cv.waitKey(0)