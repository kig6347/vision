import cv2
b=255
g=0
r=0
def blue_callback(x):
    global b
    b = cv2.getTrackbarPos('blue', 'img')

def green_callback(x):
    global g
    g = cv2.getTrackbarPos('green', 'img')

def red_callback(x):
    global r
    r = cv2.getTrackbarPos('red', 'img')

def mouse_callback(event, x, y, flags, params):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img,(x,y),10,(b,g,r),-1)
    elif event ==cv2.EVENT_MOUSEMOVE and drawing == True:
        cv2.circle(img, (x,y), 10, (b,g,r),-1)
    elif event ==cv2.EVENT_LBUTTONUP:
        drawing =False
    cv2.imshow('img',img)

drawing = False
img = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR)

if img is None:
    print("이미지 파일을 읽을 수 없습니다")
    exit(1)

cv2.imshow('img',img)
cv2.createTrackbar('blue', 'img', 0, 255, blue_callback)
cv2.createTrackbar('green', 'img', 0, 255, green_callback)
cv2.createTrackbar('red', 'img', 0, 255, red_callback)
cv2.setTrackbarPos('blue','img',255)

cv2.setMouseCallback('img', mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()
