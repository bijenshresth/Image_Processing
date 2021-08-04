#Erosion and Dilation of an image

import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread('leaf.jpg', 0)
kernel = np.ones((5,5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)
dilation = cv.dilate(img, kernel, iterations=1)

images = [img, erosion, dilation]
titles = ['Original', 'Erosion', 'Dilation']

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()