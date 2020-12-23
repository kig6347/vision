import cv2
import numpy as np

image = cv2.imread('Lenna.jpg',cv2.IMREAD_GRAYSCALE)
cols, rows = image.shape[:2]
Scaled = np.zeros((cols*2,rows*2), np.uint8)

for i in range(cols*2):
  for j in range(rows*2):
    x = int(i / 2);
    y = int(j / 2);
    Scaled[i,j] = image[x,y]
    
cv2.imshow("image",image)
cv2.imshow("Scaled",Scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
