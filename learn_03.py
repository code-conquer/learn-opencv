import cv2
img = cv2.imread('lena.jpg')
print("=========获取图像得到像素值=========")
px = img[100,30]
print(px)
px_0 = img[100,30,0]
px_1 = img[100,30,1]
px_2 = img[100,30,2]
print(px_0)
print(px_1)
print(px_2)
print("-------------------")
print(img.shape)
height,width,channels = img.shape
print(height)
print(width)
print(channels)
print(img.shape[0])
#读取图像的数据类型
print(img.dtype)

#获取总的像素数
print(img.size)  # height*width*channels

#ROI  提取感兴趣的区域
# face = img[100:300,100:300]
# cv2.imshow('face',face)
# cv2.waitKey(0)

#通道分割与合并
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
# cv2.imshow('lena',img)
# cv2.waitKey(0)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
cv2.imshow('ori',img)
cv2.waitKey(0)