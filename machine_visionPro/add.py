import cv2
import numpy as np

img1 = cv2.imread("1.png")
img2 = cv2.imread("2.jpg")
img3 = img1[:1080, :1920]
# 图像加运算，像素点相加如果大于255，则取值255（白）
img4 = cv2.add(img2, img3)
# 图像减运算， 像素点元素相减，如果值小于0则取0
img5 = cv2.subtract(img2, img3)
# 此外图像运算还有乘法、除法运算（multiply, divide）

# 加法运算，大于255则取模或减去255
# img4 += 100
cv2.imshow("window", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
