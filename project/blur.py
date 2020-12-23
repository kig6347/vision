import cv2
import numpy as np

def nothing(x):
  pass
  
img = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR)
if img is None:
  print("이미지 파일을 읽을  수 없습니다.")
  exit(1)
  
cv2.namedWindow('image')
cv2.createTrackbar('K','image',1,20, nothing)

while(1):
  if cv2.waitKey(1) & 0xFF == 27:
    break
  m = cv2.getTrackbarPos('K','image')
  
  if m == 0:
    m = 1

  mask = np.ones((m,m),np.float32)/(m*m)

dst = cv2.filter2D(img,-1,mask)
cv2.imshow('image',dst)
