import cv2
import numpy as np
#import serial


#s = serial.Serial('/dev/ttyACM0', 9600)
face_cascade = cv2.CascadeClassifier('face.xml')
cap = cv2.VideoCapture(1)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print (len(faces))
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
