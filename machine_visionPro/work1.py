# 写一个程序, 实现按l键之后拖动鼠标绘制直线, 按r键之后拖动鼠标绘制矩形, 按r键拖动鼠标绘制圆形
import cv2
import numpy as np

cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("window", 640, 480)
# zeros(row, column)
img = np.zeros((480, 640, 3), dtype=np.uint8)

initial_x = 0.0
initial_y = 0.0
end_x = 0.0
end_y = 0.0
event_flag = 0


def distance(x, y):
    return int(np.sqrt((x - initial_x) ** 2 + (y - initial_y) ** 2))


def MouseCallBack(event, x, y, flags, userdata):
    global initial_x, initial_y, end_x, end_y, event_flag
    if event == cv2.EVENT_LBUTTONDOWN:
        initial_x = x
        initial_y = y
    elif event == cv2.EVENT_LBUTTONUP:
        end_x = x
        end_y = y
        if event_flag == 1:
            cv2.line(img, (initial_x, initial_y), (end_x, end_y), (0, 0, 255), 3, 8)
        elif event_flag == 2:
            cv2.rectangle(
                img, (initial_x, initial_y), (end_x, end_y), (0, 0, 255), 3, 8
            )
        elif event_flag == 3:
            cv2.circle(
                img,
                (initial_x, initial_y),
                distance(end_x, end_y),
                (0, 0, 255),
                3,
                8,
            )
        else:
            pass


cv2.setMouseCallback("window", MouseCallBack)

while True:
    key = cv2.waitKey(1)
    if key == ord("l"):
        event_flag = 1
    elif key == ord("r"):
        event_flag = 2
    elif key == ord("c"):
        event_flag = 3
    if key == ord("q"):
        break
    cv2.imshow("window", img)

cv2.destroyAllWindows()
