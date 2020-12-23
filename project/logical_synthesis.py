import cv2 as cv

mask = cv.imread('mask.jpg', cv.IMREAD_COLOR)
img = cv.imread('Lenna.jpg', cv.IMREAD_COLOR)

cv.imshow('mask', mask)
cv.imshow('img', img)

dst = cv.bitwise_and(img, mask)
#dst = cv.bitwise_not(mask)  나 dst = cv.bitwise_or(img, mask)  나 dst = cv.bitwise_xor(img, mask) 사용가능
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()
