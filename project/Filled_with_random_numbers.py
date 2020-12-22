import cv2 as cv
import numpy as np

width = 500
height = 500

image = np.ones((height, width, 3), dtype=np.uint8)
cv.randn(image,(0,0,0),(255,255,255))

cv.imshow("result", image)
cv.waitKey(0)
