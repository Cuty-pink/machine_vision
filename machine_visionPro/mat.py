import cv2
import numpy as np

# cv2.namedWindow("img", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("img", 640, 480)
# img = cv2.imread("C:\\Users\\86182\\Desktop\\picture\\3.jpg")
# # 浅拷贝
# img2 = img.view()

# # 深拷贝
# img3 = img.copy()

# img[10:100, 10:100] = [0, 0, 255]
# cv2.imshow("img", np.hstack((img, img2, img3)))
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 在python中Mat数据对应numpy的ndarray, 使用numpy提供的深浅拷贝方法即可实现Mat的拷贝.
# shape属性中包括了三个信息
# 高度，长度 和 通道数 print(img.shape)
# 图像占用多大空间
# 高度 * 长度 * 通道数 print(img.size)
# 图像中每个元素的位深 print(img.dtype)

img4 = np.zeros((480, 640, 3), np.uint8)
# 分割通道
b, g, r = cv2.split(img4)
b[20:120, 20:120] = 255
g[10:100, 10:100] = 255

# 合并通道
img5 = cv2.merge((b, g, r))

cv2.imshow("window", img5)
cv2.waitKey(0)
cv2.destroyAllWindows()
