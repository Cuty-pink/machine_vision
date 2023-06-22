"""
Roberts算子常用来处理具有陡峭的低噪声图像, 缺点是对边缘的定位不太准确
filter2D(src, ddepth, kernel, dst = None, anchor = None, delta = None, borderType = None)
src表示输入图像  ddepth表示目标图像所需的深度  kernel表示卷积核
主要功能是通过卷积核实现对图像的卷积运算
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("dog2.jpeg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Roberts 算子
Dx = np.array([[-1, 0], [0, 1]], dtype=int)
Dy = np.array([[0, -1], [1, 0]], dtype=int)

x = cv2.filter2D(gray_img, cv2.CV_16S, Dx)
y = cv2.filter2D(gray_img, cv2.CV_16S, Dy)
# 转uint8, 图像融合
absX = cv2.convertScaleAbs(x)  # 缩放，计算绝对值，然后将结果转换为8位。
absY = cv2.convertScaleAbs(y)
Roberts = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

# 显示图形
titles = ["src", "Roberts opertor"]
images = [rgb_img, Roberts]

for i in range(2):
    plt.subplot(1, 2, i + 1)  # 将整个图像窗口分为1行2列, 当前位置为i+1.
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])  # 获取或设置当前x轴刻度位置和标签
    plt.yticks([])
plt.show()

# cv2.imshow("window1", img)
# cv2.imshow("window2", Roberts)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
