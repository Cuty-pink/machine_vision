import cv2

cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("window", 1960, 1080)
video = cv2.VideoCapture(0)
while video.isOpened():
    # 读一帧数据，返回标记和这一帧数据。True表示读到了数据，False表示没读到数据
    ret, frame = video.read()

    if not ret:
        break
    cv2.imshow("video", frame)
    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break
# 释放资源
video.release()
cv2.destroyAllWindows()
