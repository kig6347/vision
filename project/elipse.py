import numpy as np
import cv2
img = np.zeros((300, 700, 3), np.uint8)
if img is None:
    print("이미지 앱을 만들지 못함")
    exit(1)

orange = (0, 165, 255)
blue = (255, 0, 0)
magenta = (255, 0, 255)

pt1 = (120, 150)
pt2 = (550, 150)
cv2.circle(img, pt1, 1, (255, 255, 255), 1)
cv2.circle(img, pt2, 1, (255, 255, 255), 1)

cv2.ellipse(img, pt1, (100, 60), 0, 0, 360, orange, 2)
cv2.ellipse(img, pt1, (100, 60), 0, 30, 270, blue, 8)

cv2.ellipse(img, pt2, (100, 60), 30, 30, 360, orange, 2)
cv2.ellipse(img, pt2, (100, 60), 30, -30, 160, magenta, 8)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
