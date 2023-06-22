"""
中值滤波，用像素点领域灰度值的中值来代替该像素点的灰度值
优点：可以有效除去斑点噪音和椒盐噪声，均值滤波噪声也被参与运算
缺点：中值滤波时间在均值滤波的5倍以上
"""
import cv2
import numpy as np

img = cv2.imread("dog2.jpeg")
MedBlue_img = cv2.medianBlur(img, 7)
cv2.imshow("window1", img)
cv2.imshow("window2", MedBlue_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
