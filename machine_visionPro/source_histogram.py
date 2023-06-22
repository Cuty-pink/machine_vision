import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt


def grayNumber(img):
    h, w = img.shape[:2]
    grayNumber = np.zeros([256], dtype=np.uint64)
    for i in range(h):
        for j in range(w):
            grayNumber[img[i][j]] += 1
    return grayNumber


def main():
    img = cv2.imread("dog2.jpeg", 0)
    graynumber = grayNumber(img)
    x = range(256)
    plt.plot(x, graynumber, "r", linewidth=2, c="black")
    # 设置坐标轴的范围
    y_max = np.max(graynumber)
    plt.axis([0, 255, 0, y_max])
    # 设置坐标轴的标签
    plt.xlabel("gray level")
    plt.ylabel("number of pixels")
    plt.show()


main()
