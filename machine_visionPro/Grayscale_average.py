import cv2
import numpy as np

img = cv2.imread("01.jpg")
img1 = cv2.resize(img, (960, 540))
h = np.shape(img1)[0]
w = np.shape(img1)[1]

grayimg = np.zeros((h, w, 3), dtype=np.uint8)
for i in range(h):
    for j in range(w):
        grayimg[i, j] = (
            img1[i, j][0] * 0.3 + img1[i, j][1] * 0.59 + img1[i, j][2] * 0.11
        )
        # grayimg[i, j] = (img1[i, j][0] + img1[i, j][1] + img1[i, j][2]) / 3
cv2.imshow("window1", img1)
cv2.imshow("window2", grayimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
