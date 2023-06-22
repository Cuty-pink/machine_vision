# 实现图像的旋转
import cv2
import numpy as np

img = cv2.imread("dog2.jpeg", 1)


def rotate_bound(image, angle):
    # 抓取图像的尺寸，确定几何中心
    (h, w) = image.shape[:2]
    (cX, cY) = (w / 2, h / 2)
    # 抓取旋转矩阵，抓取正余弦
    # 第一个参数是旋转中心， 第二个是角度， 第三个是缩放因子
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    # 计算图像的新边界尺寸
    new_w = int((h * sin) + (w * cos))
    new_h = int((h * cos) + (w * sin))

    # 调整旋转矩阵以考虑平移
    M[0, 2] += (new_w / 2) - cX
    M[1, 2] += (new_h / 2) - cY
    # 执行实际旋转并返回图像
    res = cv2.warpAffine(image, M, (new_w, new_h))
    while 1:
        cv2.imshow("window", res)
        if cv2.waitKey(1) == ord("q"):
            break


if __name__ == "__main__":
    rotate_bound(img, 45)
