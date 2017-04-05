import cv2
import numpy as np
import imutils

d = "img/ball/"

def select_area(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print ("BGR ", img[x,y], " HSV ", img2hsv[x,y])

img = cv2.imread(d + 'ball3.jpg')
img = imutils.resize(img, width=600)
img2hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.namedWindow('image')
cv2.setMouseCallback('image', select_area)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
