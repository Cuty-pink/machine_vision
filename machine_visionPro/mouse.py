import cv2
import numpy as np

# setMouseCallback(winname, callback, userdata) winname是窗口的名字, callback是回调函数, userdata是给回调函数的参数.
# callback(event, x, y, flags, userdata)回调函数必须包含这5个参数. event是事件(鼠标移动, 左键, 右键等), x,y是点鼠标的坐标点,
# flags主要用于组合键, userdata就是上面的setMouseCallback的userdata

# 鼠标事件:
#     EVENT_MOUSEMOVE 0 鼠标移动
#     EVENT_LBUTTONDOWN 1 按下鼠标左键
#     EVENT_RBUTTONDOWN 2 按下鼠标右键
#     EVENT_MBUTTONDOWN 3 按下鼠标中键
#     EVENT_LBUTTONUP 4 左键释放
#     EVENT_RBUTTONUP 5 右键释放
#     EVENT_MBUTTONUP 6 中键释放
#     EVENT_LBUTTONDBLCLK 7 左键双击
#     EVENT_RBUTTONDBLCLK 8 右键双击
#     EVENT_MBUTTONDBLCLK 9 中键双击
#     EVENT_MOUSEWHEEL 10 鼠标滚轮上下滚动
#     EVENT_MOUSEHWHEEL 11 鼠标左右滚动
# flags:
#     EVENT_FLAG_LBUTTON 1 按下左键
#     EVENT_FLAG_RBUTTON 2 按下右键
#     EVENT_FLAG_MBUTTON 4 按下中键
#     EVENT_FLAG_CRTLKEY 8 按下ctrl键
#     EVENT_FLAG_SHIFTKEY 16 按下shift键
#     EVENT_FLAG_ALTKEY 32 按下alt键

cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("window", 1960, 1080)


# event表示触发事件，x，y表示鼠标坐标 flags鼠标的组合按键
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


cv2.setMouseCallback("window", mouse_callback, "123")

# 生成全黑图片
img = np.zeros((1080, 1960, 3), np.uint8)
while True:
    cv2.imshow("window", img)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
