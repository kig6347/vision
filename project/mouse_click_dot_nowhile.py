import numpy as np
import cv2

# 마우스 이벤트 콜백 발생 시 함수 실행
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 10, (255, 0, 0), -1) # 도형함수
        print("키눌림")
    cv2.imshow('image', img)

img = np.zeros((512,512,3), np.uint8)
# 마우스 이벤트 콜백 받을 윈도우 창
cv2.namedWindow('image')
# image 원도우에서 마우스 이벤트가 발생하면 함수 호출
cv2.setMouseCallback('image', mouse_callback)
cv2.waitKey(0)
cv2.destroyAllWindows()
