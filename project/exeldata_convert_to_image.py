import cv2
import pandas as pd
import numpy as np

data = pd.read_excel('sample.xlsx')

height, width = data.shape

ex_img = np.zeros((height, width), np.uint8)
for y in range(height):
    for x in range(width):
        ex_img[y, x] = data.values[y, x]

cv2.imshow('ex_img', ex_img)
cv2.waitKey(0)
