"""
对数变换 f(x) = c * log(1 + r(x))
"""
import cv2
import numpy as np
import math


def logtransform(c, img):
    h, w, d = img.shape[0], img.shape[1], img.shape[2]
    new_img = np.zeros((h, w, d))
    for i in range(h):
        for j in range(w):
            for k in range(d):
                new_img[i, j, k] = c * (math.log(1.0 + img[i, j, k])) - 5
    return new_img


def logtransform2(c, img):
    h, w = img.shape[:2]
    new_img = np.zeros((img.shape))
    for i in range(h):
        for j in range(w):
            new_img[i, j] = c * (math.log(1.0 + img[i, j]))
    new_img = cv2.normalize(
        new_img, new_img, 0, 255, cv2.NORM_MINMAX
    )  # 指定将图片的值放缩到 0-255 之间
    return new_img


img = cv2.imread("dog2.jpeg")
img2 = cv2.imread("dog2.jpeg", 0)
log_img1 = logtransform(1.0, img)
log_img2 = logtransform2(0.4, img2)
cv2.imshow("window1", img)
cv2.imshow("window2", log_img1)
cv2.imshow("window3", log_img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
