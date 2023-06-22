"""
之前介绍的滤波处理过程单纯地考虑空间信息，造成了边界模糊和部分信息的丢失。 
双边滤波在计算某一个像素点的新值时，不仅考虑距离信息（距离越远，权重越小），还考虑色彩信息（色彩差别越大，权重越小）。
双边滤波综合考虑距离和色彩的权重结果，既能够有效地去除噪声，又能够较好地保护边缘信息。 
在双边滤波中，当处在边缘时，与当前点色彩相近的像素点（颜色距离很近）会被给予较大的权重值；
而与当前色彩差别较大的像素点（颜色距离很远）会被给予较小的权重值（极端情况下权重可能为0，直接忽略该点），这样就保护了边缘信息。
bilateralFilter（src,d,sigmaColor,sigmaSpace,borderType）
@ src: 需要处理的图像，即原始图像。它能够有任意数量的通道，并能对各通道独立处理。
        图像深度应该是CV_8U、CV_16U、CV_16S、CV_32F或者CV_64F中的一 种。
@ d 在滤波时选取的空间距离参数，这里表示以当前像素点为中心点的直径。
    如果该值为非正数，则会自动从参数 sigmaSpace 计算得到。如果滤波空间较大（d>5），则速度较慢。
    因此，在实时应用中，推荐d=5。对于较大噪声的离线滤波，可以选择d=9。
@ sigmaColor  sigmaColor是滤波处理时选取的颜色差值范围，该值决定了周围哪些像素点能够参与到滤波中来。
            与当前像素点的像素值差值小于 sigmaColor 的像素点，能够参与到当前的滤波中。该值越大，就说明周围有越多的像素点可以参与到运算中。
            该值为0时，滤波失去意义；该值为255时，指定直径内的所有点都能够参与运算。
@ sigmaSpace sigmaSpace是坐标空间中的sigma值。它的值越大，说明有越多的点能够参与到滤波计算中来。
            当d>0时，无论sigmaSpace的值如何，d都指定邻域大小；否则，d与 sigmaSpace的值成比例。

"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import math

img = cv2.imread("dog2.jpeg")
img_bilateral = cv2.bilateralFilter(img, 0, 0.2, 40)
cv2.imshow("window1", img)
cv2.imshow("window2", img_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
