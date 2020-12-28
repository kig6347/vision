import cv2 as cv

img_color = cv.imread("kompsat-2.jpg", cv.IMREAD_COLOR)
img_gray = cv.cvtColor(img_color, cv.COLOR_BGR2GRAY)
cv.imshow("img_gray", img_gray)
img_inv= 255 - img_gray
img_color = cv.applyColorMap(img_inv,cv.COLORMAP_JET)
cv.imshow("img_color",img_color)
cv.waitKey(0)
