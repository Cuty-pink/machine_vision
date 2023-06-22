"""
在HSV模型中, 颜色是由色度(Hue), 饱和度(Saturation), 明度(Value)共同组成。
色度(Hue)使用角度度量的, 范围是从0°到360°(逆时针旋转), 比如0°代表红色, 120°代表绿色, 240°代表蓝色
饱和度(Saturation)表示颜色接近光谱色的程度。一种颜色，可以看成是某种光谱色与白色混合的结果。
其中光谱色所占的比例愈大, 颜色接近光谱色的程度就愈高, 颜色的饱和度也就愈高。其范围是0%到100%。
明度(Value)颜色明亮的程度, 对于光源色, 明度值与发光体的光亮度有关。其范围是0(暗)到1(明)。
inRange(src, lowerb, upperb[, dst]) -> dst
src 表示输入图像; lowerb 表示H、S、V的最小值; upperb 表示H、S、V的最大值
dst 表示输出图像, 与输入图像有相同的尺寸且为CV_8U类
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("dog2.jpeg")
Hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lowerb = np.array([11, 43, 46])
upperb = np.array([25, 255, 255])
split_img = cv2.inRange(Hsv_img, lowerb, upperb)
# 将二值化图像与原图进行“与”操作；实际上是提取前两个frame的“与”结果，然后输出mask为1的部分
and_img = cv2.bitwise_and(img, img, mask=split_img)  # 注意: 括号中要写mask = xxx

cv2.imshow("Hsv_img", Hsv_img)
cv2.imshow("split_img", split_img)
cv2.imshow("and_img", and_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# titles = ["Hsv_img", "split_img", "and_img"]
# images = [Hsv_img, split_img, and_img]
# for i in range(3):
#     plt.subplot(1, 3, i + 1)
#     plt.title(titles[i])
#     plt.imshow(images[i], "gray")
#     plt.xticks([])
#     plt.yticks([])
# plt.show()
