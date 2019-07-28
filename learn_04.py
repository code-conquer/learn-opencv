import cv2
img = cv2.imread('lena.jpg')
#将彩色图像转换为灰度图像
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('img',img)
# cv2.imshow('gary',img_gray)
# cv2.waitKey(0)
#图像的几何变换
# res = cv2.resize(img,(320,180))
# cv2.imshow('res',res)
# cv2.waitKey(0)
# res2 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)
# cv2.imshow('res2',res2)
# cv2.waitKey(0)
#图像翻转
# des = cv2.flip(img,0)
# cv2.imshow('ori',img)
# cv2.imshow('des',des)
# cv2.waitKey(0)

#图像的平移
# import numpy as np
rows,cols = img.shape[:2]
# M = np.float32([[1,0,100],[0,1,50]])
# des = cv2.warpAffine(img,M,(cols,rows))
# cv2.imshow('des',des)
# cv2.waitKey(0)

#图像的旋转
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,0.5)
des =cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('rot',des)
cv2.waitKey(0)

