import cv2
import numpy as np

table = np.zeros((1, 256, 3), np.int8)

for j in range(256):
    if j < 128:
        table[0, j, 0] = 255 - (j * 2)
        table[0, j, 1] = j * 2
    else:
        table[0, j, 1] = 255 - (j * 2)
        table[0, j, 2] = j * 2

img = cv2.imread("Lenna.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img[:,:,0] = gray
img[:,:,1] = gray
img[:,:,2] = gray
colorBar = cv2.LUT(img, table)
cv2.imshow("img", img)
cv2.imshow("colorBar", colorBar)
cv2.waitKey(0)
