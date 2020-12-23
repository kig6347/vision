import cv2
img = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR)

if img is None:
  print("이미지 파일을 읽을 수 없습니다.")
  exit(1)
  
img_org = img.copy()
img[:,:,0] = cv2.equalizeHist(img[:,:,0])
img[:,:,1] = cv2.equalizeHist(img[:,:,1])
img[:,:,2] = cv2.equalizeHist(img[:,:,2])
cv2.imshow("img",img)
cv2.imshow("img_org",img_org)
cv2.waitKey(0)
