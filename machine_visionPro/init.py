import cv2
import numpy


def cv_show(name, img):
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(name, 1960, 1080)
    cv2.imshow(name, img)
    key = cv2.waitKey(0)
    if key & 0xFF == ord("q"):
        cv2.destroyAllWindows()
    elif key & 0xFF == ord("s"):
        cv2.imwrite("./1.png", img)


img = cv2.imread("C:\\Users\\86182\\Desktop\\picture\\3.jpg")
cv_show("beauty", img)
