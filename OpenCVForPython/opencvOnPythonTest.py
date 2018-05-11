import numpy as np
import cv2



hah = cv2.face.createEigenFaceRecognizer()
# from matplotlib import pyplot as plt
# #load an image in grayscale
# #cv2.IMREAD_COLOR
# #cv2.IMREAD_GRAYSCALE
# #cv2.IMREAD_UNCHANGED
# img = cv2.imread('Building.bmp',0)
# #print(img)
# # [[255 255 255 ..., 255 255 255]
# #  [255 255 255 ..., 255 255 255]
# #  [255 255 255 ..., 255 255 255]
# #  ..., 
# #  [ 39  43  53 ...,  33  46  49]
# #  [ 86  85  96 ...,  34  61  49]
# #  [ 92  90  86 ...,  35  65  43]]
# print(img.shape)
# #(512, 512)
# print(img.size)
# #262144

# # show image using plt
# # plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# # plt.xticks([]), plt.yticks([])
# # plt.show()

# # show an image
# # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image',img)
# cv2.imwrite('savedImage.png',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # delete some window
# # cv2.destroyWindow('image')


