import cv2
import numpy as np

img = cv2.imread('lenna.jpg',cv2.IMREAD_COLOR)

rows, cols = img.shape[:2]

M = np.float32([[1,0,50],[0,1,50]])
#여기서 변환행렬은 2X3의 이차원 행렬입니다.
# [[1,0,x축이동],[0,1,y축이동]] 형태의 float32 type의 numpy array입니다.

dst = cv2.warpAffine(img, M,(cols, rows))
cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
