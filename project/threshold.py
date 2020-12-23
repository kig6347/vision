import cv2 as cv

img = cv.imread('lenna.png',cv.IMREAD_GRAYSCALE)

ret,mask = cv.threshold(img, 128, 255, cv.THRESH_BINARY)
cv.imshow("Original Image",img)
cv.imshow("New Image",mask)

cv.waitKey(0)
cv.destroyAllWindows()
