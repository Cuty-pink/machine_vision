"""
LOG: 高斯拉普拉斯边缘检测
特点是先将图像进行高斯滤波，然后求拉普拉斯二阶导数，通过检测滤波结果的零交叉获得图像或物体的边缘
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("dog2.jpeg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 先进性高斯滤波
GaussBlue_img = cv2.GaussianBlur(gray_img, (3, 3), 0)
# 再通过拉普拉斯算子做边缘检测
dst = cv2.Laplacian(GaussBlue_img, cv2.CV_16S, ksize=3)
LOG = cv2.convertScaleAbs(dst)

# 正常显示图像中文
plt.rcParams["font.sans-serif"] = ["SimHei"]
titles = ["原始图像", "LoG算子"]
images = [rgb_img, LOG]
for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i], "gray")
    plt.xticks([])
    plt.yticks([])
plt.show()
