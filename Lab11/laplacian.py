#Laplacian of an Image
import cv2 as cv
import numpy as np 

image = cv.imread('brickwall.jpg', 0)
image = cv.resize(image, (400, 300))
cv.imshow('Input', image)
#Using 2nd order Laplacian Operator without Gaussian Filter
imageWob = cv.Laplacian(image, cv.CV_64F, ksize=1)
cv.imshow('Output: 2nd Ord Derivative w/o Blur', imageWob)
#Using Gaussian Filter to remove Noise
blur = cv.GaussianBlur(image, (3,3), 0 )
image_blur = cv.Laplacian(blur, cv.CV_64F, ksize=1)
cv.imshow('Output: 2nd Ord Derivative', image_blur)
cv.waitKey(0)
cv.destroyAllWindows()
