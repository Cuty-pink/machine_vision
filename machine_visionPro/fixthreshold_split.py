"""
固定阈值：选取一个全局阈值，将整幅图像分成了非黑即白的二值图像
threshold(src, thresh, maxval, type[, dst])
src 表示输入图像(单通道， 8位或32位浮点型)
dst 表示输出图像(大小和类型同输入)
threshold 表示阈值   maxval 表示最大灰度值, 一般设为255
type 表示阈值化类型
enum ThresholdType{
    THRESH_BINARY        = 0, //大于阈值的部分设置为255, 小于部分设置为0
    THRESH_BINARY_INV    = 1, //大于阈值的部分设置为0, 小于部分设置为255
    THRESH_TRUNC         = 2, //大于阈值的部分设置为threshold, 小于部分保持不变
    THRESH_TOZERO        = 3, //小于阈值的部分设置为0, 大于部分保持不变
    THRESH_TOZERO_INV    = 4, //大于阈值的部分设置为0, 小于部分保持不变
    THRESH_MASK          = 5, 
    THRESH_OTSU          = 6, //自动处理， 图像自适应二值化, 常用区间为[0, 255]
    THRESH_TRIANGLE      = 7, 
}
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("dog2.jpeg")
# get gray image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 大于阈值的部分设置为255, 小于部分设置为0
threshold1 = cv2.threshold(gray_img, 170, 255, cv2.THRESH_BINARY)[1]
# or param, threshold1 = cv2.threshold(gray_img, 170, 255, cv2.THRESH_BINARY)
# 大于阈值的部分设置为0, 小于部分设置为255
threshold2 = cv2.threshold(gray_img, 170, 255, cv2.THRESH_BINARY_INV)[1]
# 大于阈值的部分设置为threshold, 小于部分保持不变
threshold3 = cv2.threshold(gray_img, 170, 255, cv2.THRESH_TRUNC)[1]
# 小于阈值的部分设置为0, 大于部分保持不变
threshold4 = cv2.threshold(gray_img, 170, 255, cv2.THRESH_TOZERO)[1]
# 大于阈值的部分设置为0, 小于部分保持不变
threshold5 = cv2.threshold(gray_img, 170, 255, cv2.THRESH_TOZERO_INV)[1]

titles = ["gray_img", "BINARY", "BINARY_INV", "TRUNC", "TOZERO", "TOZERO_INV"]
images = [gray_img, threshold1, threshold2, threshold3, threshold4, threshold5]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i], "gray")
    plt.xticks([])
    plt.yticks([])

plt.show()
