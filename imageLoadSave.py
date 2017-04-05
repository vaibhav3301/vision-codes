import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('himym.jpg',1) #BGR
img2 = img[:,:,::-1]	#RGB

plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
plt.show()

#cv2.imshow('himym', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
