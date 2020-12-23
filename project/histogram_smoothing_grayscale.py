import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)
if img is None:
  print("이미지 파일을 읽을수 없습니다.")
  exit(1)

img_org = img.copy()
img = cv2.equalizeHist(img)

cv2.imshow("img",img)
cv2.imshow("img_org",img_org)
histo_org = cv2.calcHist(img_org,[0],None,[256],[0,256])
histo_equal = cv2.calcHist(img,[0],None,[256],[0,256])

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(histo_org,color = 'b',label='histo_org')
ax2.plot(histo_equal,color = 'r',label='histo_equal')

ax1.legend(loc='upper left')
ax2.legend(loc='upper left')
plt.show()
