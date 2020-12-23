import cv2
import numpy as np

img = cv2.imread('lenna.jpg',cv2.IMREAD_COLOR)

rows, cols = img.shape[:2]

#회전할 중심 좌표 지정
center = (cols/2, rows/2)
# 이미지의 중심점을 기준으로 45도 회전 하면서 1배 Scale

M= cv2.getRotationMatrix2D(center,45,1.0)

dst = cv2.warpAffine(img, M,(cols, rows))
cv2.imshow('img', img)
cv2.imshow('Rotated', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
