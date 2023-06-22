"""
grabCut(img, mask, rect, bgdModel, fgdModel, iterCount[, mode])  -> None
参数img表示输入图像, mask表示输出掩码
mask只能取四种值: GCD_BGD(=0)表示背景, GCD_FGD(=1)表示前景,
GCD_PR_BGD(=2)表示可能的背景, GCD_PR_FGD(=3)表示可能的前景
rect表示用户选择的前景矩形区域, 包含分割对象的矩形ROL, 矩形外部像素为背景, 内部像素为前景
fgdModel表示输出前景图像, iterCount表示迭代次数
mode表示用于指示grabCut函数进行什么操作, 可选择的值有GC_INIT_WITH_RECT(=0)表示矩形窗初始化grabCut
GC_INIT_WITH_MASK(=1)表示用掩码图像初始化grabCut; GC_EVAL(=2)表示执行分割
cv2.compare(src1, src2, cmpop[, dst]) -> dst
参数src1, src2表示原始图像1,2(必须示单通道)或一个数值
dst表示结果图像, 类型示CV_8UC1, 即单通道8位图, 大小和src1和src2中最大的那个一样, 比较结果为真的地方值为255, 否则为0
cmpop表示操作类型
enum { CMP_EQ=0,    //相等
	CMP_GT=1,   //大于
	CMP_GE=2,   //大于等于
	CMP_LT=3,   //小于
	CMP_LE=4,   //小于等于
	CMP_NE=5 }; //不相等
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import warnings

warnings.filterwarnings("ignore", module="matplotlib")
imgpath = "dog2.jpeg"
img = cv2.imread(imgpath)
Coords1x, Coords1y = "NA", "NA"
Coords2x, Coords2y = "NA", "NA"


def OnClick(event):
    # 获取鼠标按下时的位置
    global Coords1x, Coords1y
    if event.button == 1:
        try:
            Coords1x = int(event.xdata)
            Coords1y = int(event.ydata)
        except:
            Coords1x = event.xdata
            Coords1y = event.ydata
        print("左上角坐标", Coords1x, Coords1y)


def OnMouseMotion(event):
    # 获取鼠标移动时的位置
    global Coords2x, Coords2y
    if event.button == 3:
        try:
            Coords2x = int(event.xdata)
            Coords2y = int(event.ydata)
        except:
            Coords2x = event.xdata
            Coords2y = event.ydata
        print("右下角坐标", Coords2x, Coords2y)


def OnMouseRelease(event):
    if event.button == 2:
        fig = plt.gca()
        img = cv2.imread(imgpath)
        # 创建一个与加载图像同形状的Mask
        mask = np.zeros(img.shape[:2], np.uint8)
        # 算法内部使用的数组, 必须创建两个np.float64类型的0数组, 大小为(1, 65)
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)
        # 计算人工前景的矩形区域(rect.x, rect.y, rect.width, rect.height)
        if (Coords2x - Coords1x) > 0 and (Coords2y - Coords1y) > 0:
            try:
                rect = (Coords1x, Coords1y, Coords2x - Coords1x, Coords2y, Coords1y)
                print("分割区域", rect)
                iterCount = 5
                cv2.grabCut(
                    img,
                    mask,
                    rect,
                    bgdModel,
                    fgdModel,
                    iterCount,
                    cv2.GC_INIT_WITH_RECT,
                )
                mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
                img = img * mask2[:, :, np.newaxis]
                plt.subpolt(121)
                plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                plt.subpolt(122)
                plt.imshow(cv2.cvtColor(cv2.imread(imgpath), cv2.COLOR_BGR2RGB))
                fig.figure.canvas.draw()
                print("May the force be with me")
            except:
                print("left click! right click")
        else:
            print("左下角坐标值必须大于右上角坐标值")
