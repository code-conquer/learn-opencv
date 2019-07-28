import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('lena.jpg')
rows, cols = img.shape[:2]
# 变换前的三个点
pts1 = np.float32([[50, 65], [150, 65], [210, 210]])
# 变换后的三个点
pts2 = np.float32([[50, 100], [150, 65], [100, 250]])
# 生成变换矩阵
M = cv2.getAffineTransform(pts1, pts2)
dst1 = cv2.warpAffine(img, M, (cols, rows))
plt.subplot(121), plt.imshow(img[:,:,::-1]), plt.title('input')
plt.subplot(122), plt.imshow(dst1[:,:,::-1]), plt.title('output')
plt.show()
