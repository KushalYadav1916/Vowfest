import cv2
import sys

imagePath = 'test2.jpg'
xml = "haarcascade_frontalface_default.xml"#the xml we use

face = cv2.CascadeClassifier(xml)

image = cv2.imread(imagePath)
#conversion in greyscale
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#face detection
faces = face.detectMultiScale(
    grey,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print("Found {0} faces!".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Image with faces',image)
cv2.waitKey(0)
