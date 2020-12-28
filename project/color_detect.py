import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
success, frame = cap.read()
  if success:
    imgThresholded = cv2.inRange(frame,(100,50,0),(255,255,100)) #파랑색 데이터 분리
    cv2.imshow("imgThresholded",imgThresholded)
    cv2.imshow("camera",frame)
    key = cv2.waitKey(10) & 0xFF
    if (key == 27):
      break
  else:
    break
cv2.waitKey(0)
cv2.destroyAllWindows()
