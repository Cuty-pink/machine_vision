import cv2
import numpy as np

img = cv2.imread("cat.jpg")
h = np.shape(img)[0]
w = np.shape(img)[1]
newimg = np.zeros((h, w, 3), dtype=np.uint8)
for i in range(h):
    for j in range(w):
        newimg[i, j] = max(img[i, j][0], img[i, j][1], img[i, j][2])

cv2.imshow("window", newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
