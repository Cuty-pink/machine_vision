import cv2
import numpy as np

cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("window", 960, 540)

img1 = cv2.imread("1.png")
img2 = cv2.imread("2.jpg")
# 拉缩变换resize，类似于图片矩阵切片 new_img1 = img1[:1080, :1920],
# resize 函数插值算法有cv2.INTER_NEARSET, cv2.INTER_LINEAR(默认), cv2.INTER_CUBIC, cv2.INTER_AREA
# new_img1 = cv2.resize(img1, (1920, 1080))
# cv2.imshow("window", np.hstack((new_img1, img2)))
# cv2.waitKey(0)
# 按照x，y轴的比例进行缩放
new_img2 = cv2.resize(img2, dsize=None, fx=0.5, fy=0.5)
cv2.imshow("window", new_img2)
cv2.imshow("window1", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
