import cv2

img = cv2.imread('Lenna.jpg', cv2.IMREAD_COLOR)
if img is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit(1)

cv2.imshow('img', img)
x = 300
y = 300
while True:
    key = cv2.waitKey(100)
    if (key == 27):
        break
    elif (key == ord('a')):
        x -= 20
    elif (key == ord('w')):
        y -= 20
    elif (key == ord('d')):
        x += 20;
    elif (key == ord('s')):
        y += 20;
    cv2.circle(img, (x, y), 100, (0, 255, 0), 5)
    cv2.imshow('img', img)

cv2.destroyAllWindows()
