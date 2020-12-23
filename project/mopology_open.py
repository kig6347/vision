import cv2
import numpy as np

img = cv2.imread('bjh.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow("Source", img)

mask=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

morphology_open = cv2.morphologyEx(img,cv2.MORPH_OPEN,mask)
morphology_close = cv2.morphologyEx(img,cv2.MORPH_CLOSE,mask)

cv2.imshow("morphology_open", morphology_open)
cv2.imshow("morphology_close", morphology_close)

open_close = cv2.morphologyEx(morphology_open,cv2.MORPH_CLOSE,mask)

cv2.imshow("open_close", open_close)
cv2.waitKey(0)
cv2.destroyAllWindows()
