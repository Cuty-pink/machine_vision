import cv2

# WINDOW_AUTOSIZE不允许修改窗口大小
# cv2.namewindow('window', cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.resizeWindow("img", 1960, 1080)
# 默认按照彩色图片读取
img = cv2.imread("C:\\Users\\86182\\Desktop\\picture\\3.jpg")
cv2.imshow("img", img)
key = cv2.waitKey(0)
if key & 0xFF == ord("q"):
    cv2.destroyAllWindows()
