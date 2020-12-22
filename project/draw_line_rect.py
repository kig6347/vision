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
p2 = (200, 200)
rec = (50, 50, 400, 400)
blue = (255, 0, 0)
red = (0, 0, 255)

cv2.rectangle(img, p1, p2, blue, -1)
cv2.rectangle(img, rec, red, 3)
cv2.rectangle(img, (300, 300), (350, 350), (0, 255, 0), 5)
cv2.line(img, p1, p2, red, 10)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
