import cv2 as cv
alpha = 0.0

while (alpha <= 1.0):
    img1 = cv.imread('maldi.jpg')
    img2 = cv.imread('Lenna.jpg')

    beta = 1.0 - alpha
    dst = cv.addWeighted(img1, alpha, img2, beta, 0)
    cv.imshow('dst', dst)
    cv.waitKey(0)
    alpha += 0.2

cv.destroyAllWindows()
