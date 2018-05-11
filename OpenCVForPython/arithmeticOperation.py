import cv2
import numpy as np
img1 = cv2.imread('Dog.bmp')
img2 = cv2.imread('Road.bmp')
dst1 = cv2.addWeighted(img1,0.5,img2,0.5,0)
cv2.imshow('dst1',dst1)
dst2 = cv2.add(img1,img2)
cv2.imshow('dst2',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
