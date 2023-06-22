import cv2
import numpy as np

img = cv2.imread("dog2.jpeg")
imgYUV = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
YUVchannels = cv2.split(imgYUV)
YUVchannels[0] = cv2.equalizeHist(YUVchannels[0])
channels = cv2.merge(YUVchannels)
result = cv2.cvtColor(channels, cv2.COLOR_YCrCb2BGR)

cv2.imshow("window1", img)
cv2.imshow("window2", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
