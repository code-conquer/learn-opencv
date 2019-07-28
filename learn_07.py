import cv2
import numpy as np
img =  np.zeros((200,200,3),np.uint8)
img1 = cv2.imread('lena.jpg')
img2 = cv2.resize(img1,(200,200),)
cv2.imshow('img2',img2)
cv2.imwrite('lena_log.jpg',img2)
#画绿色部分
cv2.ellipse(img,(43,125),(45,45),0,0,300,(0,255,0),-1,lineType=cv2.LINE_AA)
cv2.circle(img,(43,125),15,(0,0,0),-1,lineType=cv2.LINE_AA)

# 画红色的部分
cv2.ellipse(img, (90,40),(45,45),120,0,300,(0,0,255),-1,lineType=cv2.LINE_AA)
cv2.circle(img, (90, 40), 15, (0, 0, 0), -1, lineType=cv2.LINE_AA)

# 画蓝色的部分
cv2.ellipse(img,(137,125),(45,45),-60,0,300,(255,0,0),-1,lineType=cv2.LINE_AA)
cv2.circle(img, (137, 125), 15, (0, 0, 0), -1, lineType=cv2.LINE_AA)
cv2.imshow('img',img)
cv2.imwrite('cv_log.jpg',img)
cv2.waitKey(0)