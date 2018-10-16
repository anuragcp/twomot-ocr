import cv2 as cv
import numpy as np
import os

PATH_TO_FILE = "./text_data"

img = cv.imread(os.listdir(PATH_TO_FILE)[0], 0)
ret,img_otsu = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img_otsu)
cv.waitKey(0)
cv.destroyAllWindows()