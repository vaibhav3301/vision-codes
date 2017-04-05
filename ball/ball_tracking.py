
import cv2
import numpy as np
import imutils

greenLower = (29,86,6)
greenUpper = (64,255,255)
# greenLower = (165, 155, 155)
# greenUpper = (179, 255, 255)
kernel = np.ones((2,2), np.uint8)

cap = cv2.VideoCapture(0)

while True:
	(grabbed, frame) = cap.read()
	frame = imutils.resize(frame, width=600)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, kernel, iterations=2)
	mask = cv2.dilate(mask, kernel, iterations=2)

	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

	if len(cnts) > 0:
		for c in cnts:
			((x,y), radius) = cv2.minEnclosingCircle(c)
			if radius > 5:
				cv2.circle(frame, (int(x),int(y)), int(radius),(255,0,0),2)

	# cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
	# if len(cnts) > 0:
	# 	for c in cnts:
	# 		M = cv2.moments(c)


	cv2.imshow("mask", mask)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
cap.release()
cv2.destroyAllWindows()
