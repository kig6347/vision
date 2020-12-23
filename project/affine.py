import cv2
import numpy as np

def mouse_callback(event,x,y,flags, param):
    global count
    global pts1
    if event == cv2.EVENT_LBUTTONDOWN and count<4:
        print("마우스 눌림" , count)
        pts1[count][0] = x
        pts1[count][1] = y
        count += 1


color = ((255,0,0),(0,255,0),(0,0,255),(255,0,255))

cap = cv2.VideoCapture(0)

pts1 =np.zeros((4,2),np.float32)
pts2 = np.float32([[10,10],[10,500],[500,10],[500,500]])
count = 0
cv2.namedWindow("camera")
cv2.setMouseCallback('camera',mouse_callback)

while cap.isOpened():
    success, frame = cap.read()
    if success:
        for i in range(4):
            if (pts1[i][0] != 0):
                cv2.circle(frame, tuple(pts1[i]), 10, color[i], -1)

        if (count>=4):
            M = cv2.getPerspectiveTransform(pts1, pts2)
            print(pts1)
            print(pts2)
            dst = cv2.warpPerspective(frame, M, (500, 500))
            cv2.imshow('dst', dst)

        cv2.imshow("camera",frame)
        key = cv2.waitKey(10) & 0xFF
        if (key == 27):
            break
    else:
        break


cv2.waitKey(0)
cv2.destroyAllWindows()
