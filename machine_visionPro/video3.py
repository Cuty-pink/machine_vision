import cv2

cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("video", 1960, 1080)
cap = cv2.VideoCapture(0)
# avi 格式
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# videow = cv2.VideoWriter(".avi", fourcc, 30, (1960, 1080))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
# param1 : 输出视频文件
# param2 : 文件格式，eg：MP4
# param3 ：帧率
# param4 : 分辨率
videow = cv2.VideoWriter("v1.mp4", fourcc, 30, (640, 480))
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    videow.write(frame)
    cv2.imshow("video", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
videow.release()
cv2.destroyAllWindows()
