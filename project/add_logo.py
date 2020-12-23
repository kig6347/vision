import cv2 as cv

img = cv.imread('lenna.png', cv.IMREAD_COLOR)
logo = cv.imread('opencv.png', cv.IMREAD_COLOR)
logo_h,logo_w = logo.shape[:2]

img[0:logo_h,0:logo_w] = logo
cv.imshow('logo',logo)
cv.imshoe('img',img)

cv.waitKey(0)
cv.destroyWindows()
