import cv2
import numpy as np

img = cv2.imread('himym.jpg', cv2.IMREAD_COLOR)
cv2.namedWindow('image')
def sh(im):
    cv2.imshow('image', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

barney =  img[30:100,30:100]
img[200:270, 200:270] = barney

cv2.imwrite('barney.jpg', barney)
sh(img)
