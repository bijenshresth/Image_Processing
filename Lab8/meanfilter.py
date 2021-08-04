#Mean Filter

import cv2 as cv
import numpy as np 

img = cv.imread('brain.jpg', 0)

blur = cv.medianBlur(img, 7)

final = np.hstack((img, blur))

cv.imshow('final', final)
cv.waitKey(0)
cv.destroyAllWindows()

