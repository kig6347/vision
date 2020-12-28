import cv2 as cv
# 얼굴과 눈을 검출하기 위해 미리 학습시켜 놓은 분류기를 로드
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
cap = cv.VideoCapture(0) # 0: default camera
while cap.isOpened():
  success, frame = cap.read()
  if success:
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #그레이 이미지에서 얼굴 검출
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # 얼굴 검출시 좌표 정보를 리턴
    for (x, y, w, h) in faces: #얼굴에 사각형 표시
      cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
      cv.putText(frame, 'Detected Face', (x-5,y-5), 0,0.5,(255,255,0),2)
      roi_gray = gray[y:y + h, x:x + w]
      roi_color = frame[y:y + h, x:x + w]
      eyes = eye_cascade.detectMultiScale(roi_gray)
      for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv.imshow('frame', frame)
    key = cv.waitKey(10) & 0xFF
    if (key == 27):
      break
  else :
   break
cv.waitKey(0)
