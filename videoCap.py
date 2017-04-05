import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
	#frame-by-frame
	_, frame = cap.read()

	#operations on frame
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	res = cv2.bitwise_and(frame, frame, mask=mask)
	#display frame
	cv2.imshow('frame',hsv)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)

	if cv2.waitKey(15) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
