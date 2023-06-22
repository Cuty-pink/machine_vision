import cv2

cv2.namedWindow("color", cv2.WINDOW_NORMAL)
cv2.resizeWindow("color", 640, 480)
# 定义颜色空间转化表
colorspace = [
    cv2.COLOR_BGR2RGBA,
    cv2.COLOR_BGR2BGRA,
    cv2.COLOR_BGR2GRAY,
    cv2.COLOR_BGR2HSV,
    cv2.COLOR_BGR2YUV,
]


def color_callback():
    pass


img = cv2.imread("C:\\Users\\86182\\Desktop\\picture\\3.jpg")
cv2.createTrackbar("curcolor", "color", 0, 4, color_callback)

while True:
    index = cv2.getTrackbarPos("curcolor", "color")
    cvt_img = cv2.cvtColor(img, colorspace[index])
    cv2.imshow("color", cvt_img)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
