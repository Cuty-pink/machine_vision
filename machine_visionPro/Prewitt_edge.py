"""
Prewitt边缘算子是一种边缘样板算子。样板算子由理想的边缘算子图像构成，依次用边缘样板去检测图像，
与被检测区最为相似的样板给出最大值，用这个最大值作为算子的输出
Prewitt算子的原理是在图像空间利用两个方向模板与图像进行邻域卷积来完成，其中一个模板用于检测水平边缘，另一个模板检测水平边缘
优点：Prewitt算子于Sobel算子差不多，利用像素点上下、左右邻点灰度差，在边缘处达到极值检测边缘，对噪声具有平滑作用
缺点：定位精度不高
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("dog2.jpeg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Prewitt算子
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
x = cv2.filter2D(gray_img, cv2.CV_16S, kernelx)
y = cv2.filter2D(gray_img, cv2.CV_16S, kernely)

# 转为uint8, 融合图像
Prewittx = cv2.convertScaleAbs(x)
Prewitty = cv2.convertScaleAbs(y)
Prewitt = cv2.addWeighted(Prewittx, 0.5, Prewitty, 0.5, 0)

plt.rcParams["font.sans-serif"] = ["SimHei"]
titles = ["原始图像", "Prewitt算子"]
images = [rgb_img, Prewitt]

for i in range(2):
    plt.subplot(1, 2, i + 1)
    plt.imshow(images[i], "gray")  # 直接使用plt.imshow()会使图片发绿，显示时的颜色通道不是灰色通道，而是其他的通道。
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
