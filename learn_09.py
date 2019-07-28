import cv2
import numpy as np
# x = np.uint8([255])
# y = np.uint8([10])
# print(cv2.add(x,y)) >=255都是255
# print(x+y)    (x+y)%256
# 图像混合
img1 = cv2.imread('lena.jpg')
img2 = cv2.imread('cv_log.jpg')
#使用addWeighted只会改变图片的透明度
# res = cv2.addWeighted(img1,0.5,img2,0.5,0)
# res = img1+img2
# res = cv2.add(img1,img2)
# cv2.imshow('res',res)
# cv2.waitKey(0)


rows,cols = img2.shape[:2]
ROI = img1[:rows,:cols]
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_not(ROI,ROI,mask=mask_inv)
det = cv2.add(img1_bg,img2)
img1[:rows,:cols] = det
cv2.imshow('det',img1)
cv2.waitKey(0)



