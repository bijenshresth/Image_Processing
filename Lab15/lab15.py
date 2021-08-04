#Opening and Closing of an Image (Morphological Operation).

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('images.png', 0)
kernel = np.ones((13,13), np.uint8)

opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

images = [img, opening, closing]
titles = ['Original', 'Opening', 'Closing']

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()