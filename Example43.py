import cv2

cap = cv2.VideoCapture("vtest.mkv")

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('image', frame)

        key = cv2.waitKey(1000) & 0xFF
        if (key == 27):
            break
    else:
        break
    cap.release()
    cv2.destroyAllWindows()
