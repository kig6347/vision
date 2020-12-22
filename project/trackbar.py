import cv2
def nothing(x):
    pass
def mouse_callback(event, x, y, flags, param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), 10, (b, g, r), -1)
    elif event == cv2.EVENT_MOUSEMOVE and drawing == True:
        cv2.circle(img, (x, y), 10, (b, g, r), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    cv2.imshow('img', img)

drawing = False
img = cv2.imread('Lenna.jpg', cv2.IMREAD_COLOR)
if img is None:
    print("이미지 파일을 읽을 수 없습니다.")
    exit(1)

cv2.imshow('img', img)
cv2.createTrackbar('blue','img', 0, 255, nothing)
cv2.createTrackbar('green','img', 0, 255, nothing)
cv2.createTrackbar('red','img', 0, 255, nothing)
cv2.setTrackbarPos('blue','img', 255)
cv2.setMouseCallback('img', mouse_callback)
while(1):
    b = cv2.getTrackbarPos('blue', 'img')
    g = cv2.getTrackbarPos('green', 'img')
    r = cv2.getTrackbarPos('red', 'img')
    if cv2.waitKey(1) and 0xFF == 27:
        break
cv2.destroyAllWindows()
