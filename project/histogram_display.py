import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR)

if img is None:
  print("이미지 파일을 읽을 수 없습니다.")
  exit(1) 
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = cv2.calcHist([img2],[0],None,[256],[0,256])
b = cv2.calcHist([img],[0],None,[256],[0,256])
g = cv2.calcHist([img],[1],None,[256],[0,256])
r = cv2.calcHist([img],[2],None,[256],[0,256])
#3채널이라서 b,g,r을 생성해줘야한다
plt.plot(b,color = 'b',label='blue')
plt.plot(g,color = 'g',label='green')
plt.plot(r,color = 'r',label='red')
plt.plot(gray,color = 'black',label='gray')

plt.legend(loc='upper left')
cv2.imshow("img", img)
plt.show()
