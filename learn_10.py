import cv2
import numpy as np

#=======padding========
# img = np.array([[1,2,3,4],[5,6,7,8]],np.uint8)
# cons= cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_CONSTANT,value=0)
# print(img)
# print('----------')
# print(cons)
# print('----------')
# defualt = cv2.copyMakeBorder(img,1,1,1,1,cv2.BORDER_DEFAULT)
# print(defualt)

img = cv2.imread('lena.jpg')
# blur = cv2.blur(img,(3,3))
gaussian = cv2.GaussianBlur(img,(5,5),1)
median = cv2.medianBlur(img,5)
# blur1 = cv2.boxFilter(img,-1,(3,3),normalize=True)
# cv2.imshow('blur1',blur1)
# cv2.imshow('ori',img)
cv2.imshow('Ga',gaussian)
cv2.imshow('media',median)
# cv2.imshow('blur',blur)
cv2.waitKey(0)