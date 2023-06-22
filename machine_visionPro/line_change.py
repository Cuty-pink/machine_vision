"""
分段变换 f(x) =  k1 * x + c1
                k2 * x + c2
                k3 * x + c3
"""
import cv2
import numpy as np

img = cv2.imread("cat.jpg", 0)
h = np.shape(img)[0]
w = np.shape(img)[1]

out = np.zeros(img.shape, dtype=np.uint8)
for i in range(h):
    for j in range(w):
        if img[i][j] < 50:
            out[i][j] = 0.5 * img[i][j]
        elif img[i][j] < 150:
            out[i][j] = 3.6 * img[i][j] - 310
        else:
            out[i][j] = 0.238 * img[i][j] + 194

out = np.around(out)  # 对输入浮点数执行5舍6入，5做特殊处理（小数点最后一位为5的舍入为与其值最接近的偶数值）。
out = out.astype(np.uint8)  # 转换数据类型

cv2.imshow("window", img)
cv2.imshow("cat", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
