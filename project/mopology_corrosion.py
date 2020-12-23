import cv2
import numpy as np

img = cv2.imread('bjh.png',cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)
shape=cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
mask = np.array([[0,1,0],[1,1,1],[0,1,0]], np.uint8)

erode_kernel = cv2.erode(img, kernel, iterations = 1)
erode_shape = cv2.erode(img, shape, iterations = 1)
erode_mask = cv2.erode(img, mask, iterations = 1)

cv2.imshow("Source", img)
cv2.imshow("erode_kernel", erode_kernel)
cv2.imshow("erode_shape", erode_shape)
cv2.imshow("erode_mask", erode_mask)

morphologyEx_kernel = cv2.morphologyEx(img,cv2.MORPH_ERODE,kernel)
cv2.imshow("morphologyEx_kernel", morphologyEx_kernel)

cv2.waitKey(0)
cv2.destroyAllWindows()
