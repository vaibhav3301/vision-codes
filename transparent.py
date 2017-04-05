import cv2
import numpy as np

img = cv2.imread('himym.jpg')
cv2.namedWindow('image')

while True:
	cv2.imshow('image', img)
	cv2.waitKey(25)
	img[:,:,0] = img[:,:,0] + 1
	img[:,:,1] = img[:,:,1] + 1
	img[:,:,2] = img[:,:,2] + 1
