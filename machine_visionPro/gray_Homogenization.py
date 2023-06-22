import cv2
import numpy as np

img = cv2.imread("dog2.jpeg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.equalizeHist(gray_img)
cv2.imshow("window1", gray_img)
cv2.imshow("window2", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
