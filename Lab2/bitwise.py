import cv2 as cv

image1 = cv.imread("input1.jpg")
img1 = cv.resize(image1, (256, 256))
cv.imshow('image1', image1)
cv.imshow('img1',img1)

image2 = cv.imread("input2.jpg")
img2 = cv.resize(image2, (256, 256))
cv.imshow('image2', image2)
cv.imshow('img2', img2)

dest_and = cv.bitwise_and(img1, img2, mask=None)
dest_or = cv.bitwise_or(img1, img2, mask=None)
dest_xor = cv.bitwise_xor(img1, img2, mask=None)
dest_not1 = cv.bitwise_not(img1, mask=None)
dest_not2 = cv.bitwise_not(img2, mask=None)

cv.imshow('dest and', dest_and)
cv.imshow('dest or', dest_or)
cv.imshow('dest_xor', dest_xor)
cv.imshow('dest not 1', dest_not1)
cv.imshow('dest not 2', dest_not2)

cv.waitKey(0)
cv.destroyAllWindows()