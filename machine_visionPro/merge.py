import cv2
import numpy as np

img1 = cv2.imread("1.png")
img2 = cv2.imread("2.jpg")
img3 = img1[:1080, :1920]
# 偏置是将像素点的值增大或减小
new_img = cv2.addWeighted(img2, 0.3, img3, 0.7, 0)
cv2.imshow("window", new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
