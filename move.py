import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# fg = cv2.createBackgroundSubtractorMOG2()

while True:

    ret, frame = cap.read()

    # msk = fg.apply(frame)

    cv2.imshow('img', frame)
    # cv2.imshow('msk', msk)

    k = cv2.waitKey(25) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
