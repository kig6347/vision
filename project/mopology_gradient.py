import cv2
img = cv2.imread('morph_CV.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow("Source", img)

mask=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,mask)

cv2.imshow("gradient", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()
