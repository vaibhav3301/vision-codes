
import cv2
import numpy as np
import imutils

greenLower = (29,86,6)
greenUpper = (90,255,255)
kernel = np.ones((2,2), np.uint8)

frame = cv2.imread('img/ball/rov1.jpg')
frame = imutils.resize(frame, height=500, width=500)

hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, greenLower, greenUpper)
mask = cv2.erode(mask, kernel, iterations=2)
mask = cv2.dilate(mask, kernel, iterations=2)

im2, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


if len(cnts) > 0:
	for c in cnts:
		# c = max(cnts, key=cv2.contourArea)
		((x,y), radius) = cv2.minEnclosingCircle(c)
		if radius > 5:
			cv2.circle(frame, (int(x),int(y)), int(radius),(255,0,0),2)

cv2.imshow("mask", mask)
cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
