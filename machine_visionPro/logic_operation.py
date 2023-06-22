# opencv 中的非, 0反过来是255
import cv2
import numpy as np

cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("window", 840, 640)

img1 = cv2.imread("1.png")
img2 = cv2.imread("2.jpg")
# print(img1.shape)
# print(img2.shape)
# 非运算
# img1_not = cv2.bitwise_not(img1)
# cv2.imshow("window", np.hstack((img1, img1_not)))

# 与运算, 运算的图片宽高需对应
img3 = img1[:1080, :1920]
# img1_and = cv2.bitwise_and(img3, img2)
# cv2.imshow("window", np.hstack((img1_and, img3)))

# 或操作
img1_or = cv2.bitwise_or(img3, img2)
cv2.imshow("window", np.hstack((img1_or, img3)))
cv2.waitKey(0)
cv2.destroyAllWindows()
