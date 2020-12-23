import cv2
import numpy as np

img = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR)
if img is None:
  print("이미지 파일을 읽을수 없습니다.")
  exit(1)
kernel1d = cv2.getGaussianKernel(5, 1)
mask = np.outer(kernel1d, kernel1d.transpose())
print(mask)

dst = cv2.filter2D(img,-1,mask)
cv2.imshow('img',img)
cv2.imshow('Gaussian',dst)

cv2.waitKey(0)
