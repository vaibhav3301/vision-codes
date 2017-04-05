import cv2
import numpy as np

def nothing(x):
	pass

#img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('himym.jpg')
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0, 255,nothing)
cv2.createTrackbar('G','image',0, 255,nothing)
cv2.createTrackbar('B','image',0, 255,nothing)

while True:
	cv2.imshow('image', img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	r = cv2.getTrackbarPos('R','image')
	g = cv2.getTrackbarPos('G','image')
	b = cv2.getTrackbarPos('B','image')

	img[:,:,0] = cv2.add(img[:,:,0] , b)
	img[:,:,1] = cv2.add(img[:,:,1] , g)
	img[:,:,2] = cv2.add(img[:,:,2] , r)


cv2.destroyAllWindows()
