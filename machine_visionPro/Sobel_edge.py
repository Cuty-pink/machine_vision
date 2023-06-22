"""
Sobel算子利用像素上、下、左、右邻域的灰度加权算法，根据在边缘点处达到极值的原理进行边缘检测
优点：可以产生较好的检测效果， 而且对噪声具有平滑作用，可以提供较为准确的边缘方向信息
缺点：Sobel算子并没有将图像的主题和背景严格区分开
Sobel_x_or_y = cv2.Sobel(src, ddepth, dx, dy, dst, ksize, scale, delta, borderType)
src：传入的图像
ddepth：图像的深度
dx、dy：指的是求导的阶数，0表示这个方向上没有求导，所填的数一般为0、1、2。
ksize：是Sobel算子的大小，即卷积核的大小，必须为奇数1、3、5、7。如果ksize=-1，就演变成为3x3的Scharr算子，scale是缩放导数的比例常数，默认情况为没有伸缩系数。
borderType：是判断图像边界的模式，这个参数默认值为cv2.BORDER_DEFAULT。
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("dog2.jpeg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Sobel算子
x = cv2.Sobel(gray_image, cv2.CV_16S, 1, 0)
y = cv2.Sobel(gray_image, cv2.CV_16S, 0, 1)
# 转uint8， 图像融合
Sobelx = cv2.convertScaleAbs(x)
Sobely = cv2.convertScaleAbs(y)
Sobel_img = cv2.addWeighted(Sobelx, 0.5, Sobely, 0.5, 0)
# 用来正常显示中文标签
plt.rcParams["font.sans-serif"] = ["SimHei"]

titles = ["原始图像", "Sobel算子"]
images = [rgb_img, Sobel_img]
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
