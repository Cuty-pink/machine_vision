import cv2
import numpy as np

img = cv2.imread("cat2.jpeg")
img1 = cv2.resize(img, (1080, 540))
cv2.imshow("window", img)
cv2.imshow("window1", img1)
h = img.shape[0]
w = img.shape[1]
print(h, w)
cv2.waitKey(0)
cv2.destroyAllWindows()
