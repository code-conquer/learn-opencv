import cv2
# print(cv2.__version__)
#第二个参数有1，0，-1，分别代表读取的图片种类。默认1彩色图，0是灰度图
img = cv2.imread('lena.jpg',1)   #BGR

# cv2.imshow('lena',img)
# cv2.waitKey(0)
# cv2.imwrite('lena_save.jpg',img)
#打开lena.jpg并显示，如果按下’s’，就保存图片为’lena_save.bmp’，否则就结束程序。
cv2.imshow('lena.jpg',img)
s = cv2.waitKey()
if s == 115:
    cv2.imwrite('lena01.jpg',img)
else:
    print('Bey')