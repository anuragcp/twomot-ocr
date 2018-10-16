import cv2 as cv
import numpy as np
import os

#PATH_TO_FILE = "./text_data"

img = cv.imread("./text_data/ArialA.png", 0)
print("Image loaded")
ret, img_otsu = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
kernel = np.ones((5,5), np.uint8)
img_erosion = cv.erode(img, kernel, iterations=1)
img_dilation = cv.dilate(img, kernel, iterations=1)
cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
cv.imshow('image', img_dilation)
cv.waitKey(0)
cv.destroyAllWindows()
