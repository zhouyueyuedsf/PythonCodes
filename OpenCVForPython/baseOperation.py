import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('mainbuilding.jpg')
img1 = cv2.imread('Building.bmp')

# px = img[256,256]
# print(px)
# blue = img[256,256,0]
# green = img[256,256,1]
# red = img[256,256,2]
# print(blue,green,red)

# print(img.item(10,10,2))
# img.itemset((10,10,2),100)
# print(img.item(10,10,2))

# print(img.shape)
# # print(img2.shape)
# # (480, 720, 3)
# print(img.size)
# # 1036800    480*720*3=1036800
# print(img.dtype)
# # uint8

# a = img[65:120,240:440]
# img[275:330,160:360] = a

# BGR
# b = img[:,:,0] # Get the value of the blue pass
# img[:,:,2] = 0 # 假如你想使所有像素的红色通道值都为0

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# BLUE=[255,0,0]

# replicate = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_WRAP)
# constant= cv2.copyMakeBorder(img1,20,20,20,20,cv2.BORDER_CONSTANT,value=BLUE)
# plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
# plt.show()