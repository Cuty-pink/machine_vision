import cv2
import numpy as np
from matplotlib import pyplot as plt

# 读入原始图像
img = cv2.imread("dog2.jpeg", 1)
color = ("b", "g", "r")
for i, col in enumerate(color):  # enumerate可以同时获得索引和值，即 i = 0, 1, 2   col = b, g, r
    # calcHist函数可以计算多个图像、多个通道、不同灰度范围的灰度直方图
    # calcHist(imgs图像（相同深度相同大小）, channels通道, mask掩码（与图片数组大小相同）, histsize直方图维度大小, range范围)
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()
