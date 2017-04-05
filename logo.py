import numpy as np
import cv2

img = np.zeros((256,256,3), np.uint8)
size = 50
spc = 50
#red
rx = 128
ry = 64
cv2.circle(img, (rx,ry), size, (0,0,255), -1)
cv2.circle(img, (rx,ry), int(size/2.5), (0,0,0), -1)

#green
gx = rx - spc - 10
gy = ry + size + spc
cv2.circle(img, (gx,gy), size, (0,255,0), -1)
cv2.circle(img, (gx,gy), int(size/2.5), (0,0,0), -1)

#blue
bx = rx + spc + 10
by = ry + size + spc
cv2.circle(img, (bx,by), size, (255,0,0), -1)
cv2.circle(img, (bx,by), int(size/2.5), (0,0,0), -1)

pts = np.array([[rx,ry],[gx,gy],[bx,by]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.fillPoly(img, [pts], (0,0,0))

# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img, '!OpenCV', (gx-size-10, gy+size+40), font, 1, (255,255,255),3,cv2.LINE_AA)

cv2.imshow('draw', img)
cv2.imwrite('nocv.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
