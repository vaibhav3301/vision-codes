import cv2
import numpy as np


def nothing(x):
	pass


img = cv2.imread('hh.jpg')

cv2.namedWindow('image')
cv2.createTrackbar('T','image',0, 255,nothing)
while True:
	t = cv2.getTrackbarPos('T','image')
	_, th = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)

	cv2.imshow('image',th)
#cv2.imshow('image',th)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
cv2.waitKey(0)
cv2.destroyAllWindows()
