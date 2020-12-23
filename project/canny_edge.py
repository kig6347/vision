import cv2
img = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
  print("이미지 파일을 읽을 수 없습니다.")
  exit(1)

cv2.imshow("Original", img)

img_canny = cv2.Canny(img, 50, 150)
cv2.imshow("Canny Edge", img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
