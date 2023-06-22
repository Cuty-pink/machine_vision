import cv2
import numpy as np
from PIL import Image, ImageFont, ImageDraw

# cv2.namedWindow("img", cv2.WINDOW_NORMALNDO)
# cv2.resizeWindow("img", 400, 400)
img = np.zeros((400, 800, 3), dtype=np.uint8)
cv2.putText(
    img, "Hello, OpenCV", (150, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255)
)
# fill_value表示颜色填充，255是白色
img2 = np.full((400, 800, 3), fill_value=255, dtype=np.uint8)
# 导入字体文件
font = ImageFont.truetype("./STXINGKA.ttf", 25)
# 创建一个pillow图片
img_pil = Image.fromarray(img2)
draw = ImageDraw.Draw(img_pil)
# 利用draw去绘制中文
draw.text((100, 150), "你好，机器视觉", font=font, fill=(0, 0, 0, 0))
# 重新变回ndarray
img3 = np.array(img_pil)

imgs = np.hstack([img, img3])

cv2.imshow("window", imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 增加边框
img4 = cv2.copyMakeBorder(
    img3, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=(255, 0, 255)
)
cv2.imshow("window1", img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
