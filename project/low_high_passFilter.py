import cv2
import numpy as np

def displayDFT(name,src):
  src1 = src[:,:,0];
  src2 = src[:, :, 1];
  mag_image = cv2.magnitude(src1,src2)
  mag_image += 1
  spectrum = np.log(np.abs(mag_image))
  dft = cv2.normalize(spectrum,None,0,1,cv2.NORM_MINMAX)
  cv2.imshow(name,dft)

img = cv2.imread('lenna.jpg',cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape
crow,ccol = int(rows/2), int(cols/2)

lowpass = np.zeros((rows,cols,2),np.float32)
cv2.circle(lowpass,(crow,ccol),50,(1,1),-1)
highpass = np.ones((rows,cols,2),np.float32)
cv2.circle(highpass,(crow,ccol),50,(0,0),-1)

dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

fshift = cv2.multiply(dft_shift,lowpass) #lowpass 필터 적용
#highpass 필터로 변경가능

f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,0])
idft = cv2.normalize(np.abs(img_back),None,0,1,cv2.NORM_MINMAX)

displayDFT("DFT2",dft_shift)
displayDFT("DFT",fshift)

cv2.imshow("org",img)
cv2.imshow("inverted",idft)
cv2.waitKey(0)
