import numpy as np
import cv2

# Create a blace image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img,(0,0),(256,256),(255,0,0),5)
cv2.rectangle(img,(128,128),(384,384),(0,255,0),0)
cv2.circle(img,(256,256),128,(0,0,255),0)
# cv2.circle(img,(256,256),128,(0,0,255),-1) # will fullfill the circle
cv2.ellipse(img,(256,256),(100,50),30,0,180,255,-1)
# 椭圆沿逆时针方向旋转的角度。椭圆弧演顺时针方向起始的角度和结束角度，如果是0 很360，就是整个椭圆。

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
# 这里reshape 的第一个参数为-1, 表明这一维的长度是根据后面的维度的计算出来的。

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(256,256), font, 1,(255,255,255),2)
# img, text, position, font, size, color, thin

cv2.imshow('drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()