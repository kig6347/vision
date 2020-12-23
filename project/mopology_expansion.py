import cv2
import numpy as np
img = cv2.imread('bjh.png',cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5, 5), np.uint8)
dilate_kernel = cv2.dilate(img, kernel, iterations = 1)

cv2.imshow("Source", img)
cv2.imshow("dilate_kernel", dilate_kernel)
cv2.waitKey(0)
cv2.destroyAllWindows()
