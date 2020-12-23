import cv2 as cv
import numpy as np

table = np.zeros((256), np.uint8)
r = 0.04
for i in range(256):
  table[i] = pow(i / 255.0, r) * 255.0

img = cv.imread('lenna.jpg', cv.IMREAD_COLOR)
  
imgGamma=cv.LUT(img,table)
cv.imshow("img",img)
cv.imshow("imgGamma",imgGamma)

cv.waitKey(0)
