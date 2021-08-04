# Gaussian noise addition in an Image
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('camera.png', 0)
row, col = img.shape
print(img.shape)
gauss = np.random.normal(10, 10, (row, col))
noisy = img + gauss

plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(img, cmap='gray')
plt.title('Gaussian Noise Image '), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.hist(noisy.ravel(), 256, [0, 256])
plt.title('Noisy Image Histogram'), plt.xticks([]), plt.yticks([])
plt.show()