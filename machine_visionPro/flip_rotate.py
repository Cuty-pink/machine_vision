import cv2
import numpy as np

img = cv2.imread("cat.jpg")
img2 = cv2.resize(img, (640, 480))
# flipCode = 0, 表示上下翻转
# flipCode > 0, 表示左右翻转
# flipCode < 0, 表示上下左右翻转
# img1 = cv2.flip(img2, flipCode=0)
# cv2.imshow("window", np.hstack((img2, img1)))

# ROTATE_90_CLOCKWISE           顺时针旋转90°
# ROTATE_180                    旋转180°
# ROTATE_90_COUNTERCLOCKWISE    逆时针旋转90°

img1 = cv2.rotate(img2, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow("window", img2)
cv2.imshow("window1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
