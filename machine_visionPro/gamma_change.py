"""
伽马变换(gamma)      f(x) = c * r(x) * γ
"""
import cv2
import numpy as np
import math
import copy

img = cv2.imread("dog2.jpeg")
# 灰度化处理
img1 = cv2.imread("dog2.jpeg", 0)
# 灰度化处理： 用于图像二值化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 伽马变换
gamma = copy.deepcopy(gray)
rows = img.shape[0]
cols = img.shape[1]
for i in range(rows):
    for j in range(cols):
        gamma[i][j] = 3 * pow(gamma[i][j], 0.8)
cv2.imshow("window1", img)
cv2.imshow("window2", img1)
cv2.imshow("window3", gamma)
cv2.waitKey(0)
cv2.destroyAllWindows()
