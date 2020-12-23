import cv2 as cv

img = v.imread('lenna.png', cv.IMREAD_COLOR)
if img is None:
  print("이미지 파일을 읽을 수 없습니다.")
  exit(1)

res1 = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC)
# 옵션 지정 할때 interpolation은 꼭 쓸것
#OR
height, width = img.shape[:2]
res2 = cv.resize(img,(heigh*2, width*2), interpolation = cv.INTER_CUBIC)

cv.imshow("img",img)
cv.imshow("res1",res1)
cv.imshow("res2",res2)
cv.waitKey(0)
