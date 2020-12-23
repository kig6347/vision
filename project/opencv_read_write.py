import cv2

img_basic = cv2.imread('lenna.jpg',cv2.IMREAD_COLOR)
if img_basic is Nonw:
  print("이미지 파일을 읽을 수 없습니다.")
  exit(1)

cv2.imshow('Image Basic',img_basic)
cv2.waitKey(0)

cv2.imwrite('result1.png',img_basic)

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Gray',img_gray)
cv2.waitKey(0)

cv2.imwrite('result2.png',img_gray)
cv2.destroyAllWindows()
