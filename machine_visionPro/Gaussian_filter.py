"""
手工实现高斯滤波, 利用公式进阿里二维高斯卷积核
"""
import cv2
import numpy as np
import math


# 灰度化处理
def rgb2gray(img):
    h, w = img.shape[:2]
    gray_img = np.zeros((h, w), np.uint8)
    for i in range(h):
        for j in range(w):
            gray_img[i][j] = (
                img[i, j, 0] * 0.144 + img[i, j, 2] * 0.299 + img[i, j, 1] * 0.587
            )
    return gray_img


# 计算高斯卷积核
def gaussianKernel(size):
    sigma = 1.0
    gaussiankernel = np.zeros((size, size), np.float32)
    for i in range(size):
        for j in range(size):
            norm = math.pow(1 - i, 2) + math.pow(1 - j, 2)
            gaussiankernel[i, j] = math.exp(-norm / (2 * sigma * sigma))
    sum = np.sum(gaussiankernel)
    kernel = gaussiankernel / sum
    return kernel


# 高斯滤波
def gauss(img):
    h, w = img.shape[:2]
    img1 = np.zeros((h, w), np.uint8)
    kernel = gaussianKernel(3)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            sum = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    sum += img[i + k, j + l] * kernel[k + 1, l + 1]
            img1[i, j] = sum
    return img1


img = cv2.imread("dog2.jpeg")
grayimg = rgb2gray(img)
guassimg = gauss(grayimg)
cv2.imshow("window1", img)
cv2.imshow("window2", grayimg)
cv2.imshow("window3", guassimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
