#To Plot The Magnitude Spectrum

import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt

img = cv.imread('leaf.jpg', 0)
img = np.float32(img)

dft = cv.dft(img, flags=cv.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

magnitude_spectrum = 20 * np.log(cv.magnitude(dft_shift[:,:, 0], dft_shift[:,:,1]))

images = [img, magnitude_spectrum]
titles = ['Original', 'Magnitude Spectrum']

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()