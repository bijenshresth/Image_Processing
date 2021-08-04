#Applying Sobel Filter in an image

import cv2 as cv

image = cv.imread('brickwall.jpg', 0)
image = cv.resize(image, (400, 300))
cv.imshow('Input', image)

image1 = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=1)#x-direction
image2 = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=1)#y-direction
cv.imshow('Output: Sobel X axis', image1)
cv.imshow('Output: Sobel Y axis', image2)


cv.waitKey(0)
cv.destroyAllWindows()