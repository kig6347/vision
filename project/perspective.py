import cv2
import numpy as np
img = cv2.imread('affine_test.png',cv2.IMREAD_COLOR)

rows, cols = img.shape[:2]

pts1 = np.float32([[125,190],[115,310],[360,140],[360,360]])
pts2 = np.float32([[10,10],[10,500],[500,10],[500,500]])
# pts1의 좌표에 표시. perspective 변환후 이동점 확인

cv2.circle(img, (125,190), 10, (255,0,0),-1)
cv2.circle(img, (115,310), 10, (0,255,0),-1)
cv2.circle(img, (360,140), 10, (0,0,255),-1)
cv2.circle(img, (360,360), 10, (0,0,0),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (500,500))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
