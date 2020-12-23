import cv2
import numpy as np

img = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
  print("이미지 파일을 읽을 수 없습니다.")
  exit(1)
histogram = table = np.zeros((256))
height, width = img.shape

for y in range(height):
  for x in range(width):
    histogram[img[y,x]] +=1

for i in range(255):
  print("index = %d , count = %d " % (i ,histogram[i]))
