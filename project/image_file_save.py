import cv2

img_color = cv2.imread('sample.bmp', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

height, width = img_gray.shape

f = open('image.txt', 'w')

for y in range(height):
    for x in range(width):
        print("%3d" % img_gray[y, x], end=" ")
        f.write("%3d " % img_gray[y, x])
    print("")
    f.write("\n")

f.close()
cv2.imshow("Binary", img_gray)
cv2.waitKey(0)
