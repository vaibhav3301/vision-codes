import cv2
import numpy as np

def nothing(x):
	pass

img1 = cv2.imread('cnv.jpg')
img2 = cv2.imread('nocv.jpg')
cv2.namedWindow('image')

cv2.createTrackbar('thresh','image',25,255,nothing)


while True:
	cv2.imshow('image',img1)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	th = cv2.getTrackbarPos('thresh','image')
	r1, c1, _ = img2.shape
	r2, c2, _ = img1.shape
	roi = img1[int(r2/2)-int(r1/2):int(r2/2)+int(r1/2), int(c2/2)-int(c1/2):int(c2/2)+int(c1/2)]
	i2g = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
	_, mask = cv2.threshold(i2g, th, 255, cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)
	img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
	img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
	dst = cv2.add(img1_bg, img2_fg)
	img1[int(r2/2)-int(r1/2):int(r2/2)+int(r1/2), int(c2/2)-int(c1/2):int(c2/2)+int(c1/2)] = dst
    # cv2.imshow('i2g', i2g)
    # cv2.imshow('mask',mask)
    # cv2.imshow('mask_inv',mask_inv)
    # cv2.imshow('img1_bg',img1_bg)
    # cv2.imshow('img2_fg',img2_fg)
    # cv2.imshow('dst',dst)

cv2.destroyAllWindows()
