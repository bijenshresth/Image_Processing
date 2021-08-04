# Denoising an Image
import numpy as np 
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('veg.png')
dst = cv.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(dst)
plt.show()

