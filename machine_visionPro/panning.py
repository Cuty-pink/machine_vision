# 图像的平移
import cv2
import numpy as np

img = cv2.imread("dog2.jpeg", 1)
rows, cols, channels = img.shape
M = np.float32([[1, 0, 100], [0, 1, 50]])
res = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("window", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
