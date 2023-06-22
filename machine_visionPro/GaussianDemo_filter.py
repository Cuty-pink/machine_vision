import cv2
import numpy as np
import math

ksize = 1
sigma = 15
window_name = "Gaussian Demo"


def GaussianBlueSize(GaussianBlur_size):
    global ksize
    ksize = GaussianBlur_size * 2 + 3
    print(ksize, sigma)
    dst = cv2.GaussianBlur(img, (ksize, ksize), sigma, ksize)
    cv2.imshow(window_name, dst)


def GaussianBlurSigma(GaussianBlur_sigma):
    global sigma
    sigma = GaussianBlur_sigma / 10
    print(ksize, sigma)
    dst = cv2.GaussianBlur(img, (ksize, ksize), sigma, ksize)
    cv2.imshow(window_name, dst)


GaussianBlue_size = 1
GaussianBlue_sigma = 15
max_value = 300
max_type = 6

img = cv2.imread("dog2.jpeg", 0)
cv2.namedWindow(window_name)

# 创建滑动条
cv2.createTrackbar(
    "trackbar_size", window_name, GaussianBlue_size, max_value, GaussianBlueSize
)
cv2.createTrackbar(
    "trackbar_sigma", window_name, GaussianBlue_sigma, max_type, GaussianBlurSigma
)

# 初始化
GaussianBlueSize(1)
GaussianBlurSigma(15)

while True:
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
