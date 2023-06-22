import cv2
import numpy as np

# line(img, pt1, pt2, color, thickness, lineType, shift) 画直线
#     img: 在哪个图像上画线
#     pt1, pt2: 开始点, 结束点. 指定线的开始与结束位置
#     color: 颜色
#     thickness: 线宽
#     lineType: 线型.线型为-1, 4, 8, 16, 默认为8
#     shift: 坐标缩放比例.
# rectangle() 参数同上 画矩形
# circle(img, center, radius, color[, thickness[, lineType[, shift]]]) 中括号内参数表示可选参数. 画圆
# ellipse(img, 中心点, 长宽的一半, 角度, 从哪个角度开始, 从哪个角度结束,...)
# polylines(img, pts, isClosed, color[, thickness[, lineType[, shift]]]) 画多边形
# fillPoly 填充多边形
# putText(img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]) 绘制文本
#     text 要绘制的文本
#     org 文本在图片中的左下角坐标
#     fontFace 字体类型即字体
#     fontScale 字体大小


img = np.zeros((480, 640, 3), np.uint8)
cv2.line(img, (50, 50), (100, 100), (0, 52, 135), 2)
cv2.rectangle(img, (20, 20), (100, 100), (0, 0, 255))
cv2.circle(img, (200, 200), 20, (255, 0, 0))
cv2.ellipse(img, (150, 140), (100, 50), 60, 0, 360, (0, 255, 36))

# 绘制丰田车标
cv2.ellipse(img, (180, 180), (160, 100), 0, 0, 360, (0, 0, 255), 5, 8)
cv2.ellipse(img, (180, 180), (100, 44), 90, 0, 360, (0, 0, 255), 5, 8)
cv2.ellipse(img, (180, 128), (112, 48), 0, 0, 360, (0, 0, 255), 5, 8)

# 多边形, pts多边形的点集必须是int32位, True 表示闭合
pts = np.array([((60, 52), (86, 45), (46, 82))], dtype=np.int32)
# cv2.polylines(img, [pts], True, (0, 0, 255), 4)
cv2.polylines(img, [np.int32([(60, 52), (86, 45), (46, 82)])], True, (0, 0, 255), 4)
# 填充多边形
cv2.fillPoly(img, [np.int32([(120, 120), (210, 150), (180, 180)])], (255, 255, 255), 4)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
