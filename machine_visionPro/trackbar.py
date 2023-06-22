import cv2
import numpy as np

# createTrackbar(trackbarname, winname, value, count, onChange) 创建TrackBar控件, value为trackbar的默认值, count为bar的最大值, 最小为0
# getTrackbarPos(trackbarname, winname) 获取TrackBar当前值


cv2.namedWindow("trackbar", cv2.WINDOW_NORMAL)
cv2.resizeWindow("trackbar", 640, 480)


# 定义回调函数
def callback(value):
    print(value)


# 创建三个trackbar
cv2.createTrackbar("R", "trackbar", 0, 255, callback)
cv2.createTrackbar("G", "trackbar", 0, 255, callback)
cv2.createTrackbar("B", "trackbar", 0, 255, callback)

img = np.zeros((480, 640, 3), np.uint8)
while True:
    # 获取当前trackbar的值q
    r = cv2.getTrackbarPos("R", "trackbar")
    g = cv2.getTrackbarPos("G", "trackbar")
    b = cv2.getTrackbarPos("B", "trackbar")

    img[:] = [b, g, r]
    cv2.imshow("trackbar", img)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
