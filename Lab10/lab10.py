import cv2 as cv
import numpy as np 

image = cv.imread('eye.jpg', 0)
gauss_mask = cv.GaussianBlur(image, (15,15), 0)
image_sharp = cv.addWeighted(image, 2, gauss_mask, -1,  0)
kernel = np.array([[-1,-1,-1],
                  [-1,8,-1],
                  [-1,-1,-1]])
image_hpf= cv.filter2D(image, -1, kernel)

cv.imshow('output', np.vstack((image, image_hpf,  image_sharp)))
cv.waitKey(0)
cv.destroyAllWindows()