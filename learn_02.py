import cv2
img = cv2.imread('lena.jpg')
#资源http://ex2tron.wang/opencv-python-extra-high-quality-save-and-using-matplotlib/
#bmp
cv2.imwrite('lena.bmp',img)  #800KB
#jpg 默认95%质量
cv2.imwrite('img_jpg95.jpg',img) #93.6KB
#jpg 20%质量
cv2.imwrite('img_jpg20.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),20])   #12.6KB
#jpg 100%质量
cv2.imwrite('img_jpg100.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),100])  #169KB

#png 默认1压缩比
cv2.imwrite('img_png1.png',img)  #412KB

#png 压缩比9
cv2.imwrite('img_png9.png',img,[int(cv2.IMWRITE_PNG_COMPRESSION),9])  #382KB
