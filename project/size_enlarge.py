import cv2
import numpy as np
image = cv2.imread('Lenna.jpg',cv2.IMREAD_GRAYSCALE)

cols, rows = image.shape[:2]
Scaled = np.zeros((cols*2,rows*2), np.uint8)

for i in range(cols):
  for j in range(rows):
    x = i * 2;
    y = j * 2;
    Scaled[x,y] = image[i,j]
    
cv2.imshow("image",image)
cv2.imshow("Scaled",Scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
