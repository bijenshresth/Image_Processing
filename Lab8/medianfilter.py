#Median Filter

import cv2 as cv
import numpy as np 

img = cv.imread('saltpepper.jpg', 0)

blur = cv.medianBlur(img, 3)

final = np.hstack((img, blur))

cv.imshow('final', final)
cv.waitKey(0)
cv.destroyAllWindows()

