import cv2

cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("video", 1960, 1080)
video = cv2.VideoCapture("")
while video.isOpened():
    ret, frame = video.read()
    key = cv2.waitKey(1)
    if not ret:
        break
    cv2.imshow("video", video)
    if key == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
