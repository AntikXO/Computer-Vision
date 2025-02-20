import os
import cv2 as cv
import numpy as np

pieces = ["Bishop", "King", "Knight", "Pawn", "Queen", "Rook"]
DIR = r"C:\Users\Antik\Python\OpenCV\Chess"
haar_cascade = cv.CascadeClassifier("haar_faces.xml")

features = []
labels = []

def create_train():
    for name in pieces:
        path = os.path.join(DIR, name)
        label = pieces.index(name)

        for img in os.listdir(path):
            if not img.lower().endswith(('.png', '.jpg', '.jpeg')):  # Only process image files
                continue

            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)

            if img_array is None:
                print(f"Warning: Unable to read image {img_path}")
                continue  # Skip if image not loaded

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("TRAINING DONE")

features=np.array(features,dtype="object")
labels=np.array(labels)

chess_piece_recognizer=cv.face.LBPHFaceRecogniser.create()

chess_piece_recognizer.train(features,labels)

np.save("features.npy",features)
np.save("labels.npy",labels)