import cv2 as cv

img = cv.imread('lenna.png',cv.IMREAD_GRAYSCALE)

cv.imshow("img",img+100)
cv.imshow("img.add",cv.ass(img,100))
cv.imshow("inverse_img",255-img)
cv.waitKey(0)
