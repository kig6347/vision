import cv2

img_color = cv2.imread('sample.bmp', cv2.IMREAD_COLOR)

height, width, channel = img_color.shape

for y in range(height):
    for x in range(width):
        print("%3d" % img_color[y, x, 0], end=" ")
        print("%3d" % img_color[y, x, 1], end=" ")
        print("%3d" % img_color[y, x, 2], end=" ")
    print("")


cv2.imshow("img_color", img_color)
cv2.waitKey(0)
