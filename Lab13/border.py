#Padding in an image (Making Borders of an Image)

import cv2 as cv
import matplotlib.pyplot as plt
RED = [255, 0, 0]

img = cv.imread('opencv_logo.jpg')

replicate = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=RED)

images = [img, replicate, reflect, reflect101, wrap, constant]
titles = ['Original', 'Replicate', 'Reflect', 'Reflect 101', 'Wrap', 'Constant']
for i in range(6):
    plt.subplot(2 , 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()