import cv2 as cv

img =cv.imread('lenna.png', cv.IMREAD_COLOR)
if img is None:
  print("이미지 파일을 읽을 수 없습니다.")
  exit(1)
  

roi = img[10:100,10:100]
cv.imshow("roi",roi)

img[10:100,10:100] = 0
cv.imshow('img',img)

cv.waitKey(0)
cv.destroyWindows()
