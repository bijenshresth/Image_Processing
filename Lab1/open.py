import cv2 as cv

img = cv.imread("download.png")
img_gray = cv.imread("download.png", 0)

cv.imshow('image', img)
cv.imshow('gray image', img_gray)

cv.waitKey(0)
cv.destroyAllWindows()


print("Shape of Original Image: ", img.shape)
print(img[:,:,0])
print("Shape of Gray Scale Image:", img_gray.shape)
print(img_gray[:,:])