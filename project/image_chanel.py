import copy
import cv2

img_org = cv2.imread('apple.png', cv2.IMREAD_COLOR)

# B, G, R 중 한가지 색만 출력
cv2.imshow('single', img_org[:, :, 2])
img_ch = copy.deepcopy(img_org) # 복사 방법

# B, R 색상 반전
img_ch[:, :, 0] = img_org[:, :, 2]
img_ch[:, :, 2] = img_org[:, :, 0]
cv2.imshow('reversal', img_ch)

# B G R 색상 변경
img_org[:, :, 2] = 255
cv2.imshow('change', img_org)

cv2.waitKey(0)
