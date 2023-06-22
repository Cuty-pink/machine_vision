"""
自适应阈值: 根据图像不同区域亮度分布计算其局部阈值
自适应阈值分割是对图像中的各个部分进行分割, 即采用邻域分割, 在一个邻域范围内进行图像阈值分割
adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
src 表示源图像, dst表示输出图像, 与源图像大小一致
maxValue 表示预设满足条件的最大值; 
adaptiveMethod 表示指定自适应阈值算法, 可选择ADAPTIVE_THRESH_MEAN_C 或 ADAPTIVE_THRESH_GAUSSIAN_C两种
ADAPTIVE_THRESH_MEAN_C 为局部邻域块的平均值, 该算法是先求出块中的均值, 再减去常数C
ADAPTIVE_THRESH_GAUSSIAN_C 为局部邻域块的高斯加权和, 该算法是在区域中(x, y)周围的像素根据高斯函数按照它们离中心点的距离进行加权计算, 再减去常数C
thresholdType指定阈值类型, 可选择THRESH_BINARY 或 THRESH_BINARY_INV两种(二进制阈值或反二进制阈值)
blocksize表示邻域块大小, 用来计算区域阈值, 一般选择为3、5、7
C 表示与算法有关的参数, 是一个从均值或加权均值提取的常数, 可以是负数
自适应阈值化计算的过程是为每一个像素点单独计算阈值, 即每个像素点的阈值都是不同的, 就是将该像素点周围BXB区域内的像素加权平均, 然后再减去一个常数C, 从而得到该点的阈值

"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("dog2.jpeg")
# get gray image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
maxValue = 255
blockSize = 3
constValue = 10
adaptiveMethod = 1  # 0: ADAPTIVE_THRESH_MEAN_C ; 1: ADAPTIVE_THRESH_GAUSSIAN_C
thresholdType = 1  # 0: THRESH_BINARY  1: THRESH_BINARY_INV
adaptiveM_img = cv2.adaptiveThreshold(
    gray_img, maxValue, adaptiveMethod, thresholdType, blockSize, constValue
)
fixThreh_img = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY)[1]
titles = ["gray_img", "fixThreh_img", "adaptiveM_img"]
images = [gray_img, fixThreh_img, adaptiveM_img]
for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i], "gray")
    plt.xticks([])
    plt.yticks([])
plt.show()
