"""
均值滤波，首先要考虑需要对周围多少个像素点取平均值。通常情况下, 以当前像素点为中心,
对行数和列数相等的一块区域内的所有像素点的像素值求平均。
cv2.blur(src, ksize, dst, anchor, borderType)
src表示输入图像, ksize表示滤波模板kernel的尺寸, dst表示输出图像
anchor是锚点, 其默认值是(-1,-1),表示当前计算均值的点位于核的中心点位置。该值使用默认值即可, 在特殊情况下可以指定不同的点作为锚点。
borderType是边界样式, 该值决定了以何种方式处理边界。一般情况下不需要考虑该值的取值, 直接采用默认值即可。

"""
import cv2
import numpy as np

TrackbarMaxValue = 9
TrackbarMinValue = 0
KernelValue = 0
WindowName = "mean filter"
TrackbarName = "kernel"
img = cv2.imread("dog2.jpeg")
result_img = cv2.imread("dog2.jpeg")


def TrackbarCallback(x):
    global KernelValue
    global result_img
    # 根据输入值重新计算kernel（核）尺寸
    Cur_TrackbarValue = cv2.getTrackbarPos(TrackbarName, WindowName)
    kernelValue = Cur_TrackbarValue * 2 + 1
    # 均值滤波函数
    ksize = (kernelValue, kernelValue)
    cv2.blur(img, ksize, result_img)


cv2.namedWindow(WindowName)
cv2.createTrackbar(TrackbarName, WindowName, 0, 9, TrackbarCallback)
while True:
    cv2.imshow(WindowName, result_img)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
