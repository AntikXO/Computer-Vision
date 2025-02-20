import cv2 as cv

img=cv.imread("Photos/young-bearded-man-with-striped-shirt.jpg")
img=cv.resize(img,(1200,800),interpolation=cv.INTER_CUBIC)
cv.imshow("Resized",img)

# gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

haar_cascade=cv.CascadeClassifier("haar_faces.xml")
faces_rect=haar_cascade.detectMultiScale(img,scaleFactor=1.1,minNeighbors=6)

for [x,y,w,h] in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=3)

cv.imshow("Detected_Faces",img)

total_faces=print(len(faces_rect))
print(faces_rect)

cv.waitKey(0)