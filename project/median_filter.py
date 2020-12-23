import cv2
img = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR)

if img is None:
  print("이미지 파일을 읽을 수 없습니다.")
  exit(1)
  
blur = cv2.medianBlur(img,5)

cv2.imshow('img',img)
cv2.imshow('median',blur)
cv2.waitKey(0)
