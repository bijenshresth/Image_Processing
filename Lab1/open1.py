import cv2 as cv

img = cv.imread("cat.png")
img_r = cv.resize(img, (354, 354))
img_gray = cv.imread("cat.png", 0)
img_gr = cv.resize(img_gray, (354, 354))
cv.imshow('image', img_r)
cv.imshow('gray image', img_gr)

cv.waitKey(0)
cv.destroyAllWindows()


print("Shape of Original Image: ", img_r.shape)
print(img_r[:,:,0])
print("Shape of Gray Scale Image:", img_gr.shape)
print(img_gr[:,:])