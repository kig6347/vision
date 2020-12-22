import numpy as np
import cv2

width = 500
height = 500
bpp = 3

img = np.zeros((height, width, bpp), np.uint8)
if img is None:
    print("이미지 앱을 만들지 못함")
    exit(1)

p1 = (100, 100)
blue = (255, 0, 0)
red = (0, 0, 255)

cv2.circle(img, p1, 50, red, -1)
cv2.circle(img, (250, 250), 100, (0, 255, 0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
