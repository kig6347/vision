import numpy as np
import cv2

img = np.zeros((300, 700, 3), np.uint8)
if img is None:
    print("이미지 앱을 만들지 못함")
    exit(1)

blue = (255, 0, 0)

p1 = (200, 100)
cv2.putText(img, 'OpenCV', p1, 0, 2, blue, 5)
p1 = (200, 200)
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cv2.putText(img, 'OpenCV', p1, font, 2, blue, 2)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
