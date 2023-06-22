import cv2
import numpy as np

img = cv2.imread("2.jpg")
logo = np.zeros((100, 100, 3), dtype=np.uint8)
cv2.ellipse(logo, (45, 45), (40, 25), 0, 0, 360, (0, 255, 255), 5, 8)
cv2.ellipse(logo, (45, 45), (25, 11), 90, 0, 360, (0, 255, 255), 5, 8)
cv2.ellipse(logo, (45, 32), (28, 12), 0, 0, 360, (0, 255, 255), 5, 8)

# 掩码mask(黑白图),
mask = np.zeros((100, 100), dtype=np.uint8)
cv2.ellipse(mask, (45, 45), (40, 25), 0, 0, 360, 255, 5, 8)
cv2.ellipse(mask, (45, 45), (25, 11), 90, 0, 360, 255, 5, 8)
cv2.ellipse(mask, (45, 32), (28, 12), 0, 0, 360, 255, 5, 8)
# 取非
mask_not = cv2.bitwise_not(mask)
# 选择图片logo的添加位置
roi = img[:100, :100]
# roi与运算，将运算后的结果与mask_not相与，如果结果为True，则返回原图像素，否则返回0(黑)
dst = cv2.bitwise_and(roi, roi, mask=mask_not)
# img上获得logo上标
emb = cv2.add(dst, logo)
img[:100, :100] = emb

cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
