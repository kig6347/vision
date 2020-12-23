import cv2
import numpy as np

img = cv2.imread('lenna.jpg',cv2.IMREAD_COLOR)

rows, cols, ch = img.shape
pts1 = np.float32([[0,0],[511,0],[0,511]])
pts2 = np.float32([[0,150],[400,100],[100,300]])

cv2.circle(img, (0 +10,0 +10), 10, (255,0,0),-1)
cv2.circle(img, (511 -10,0 +10), 10, (0,255,0),-1)
cv2.circle(img, (0 +10,511 -10), 10, (0,0,255),-1)

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols,rows))

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
