#Implementation of Gaussian High Pass Filter 

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("smile.jpg", 0)
min = np.minimum(img.shape[0], img.shape[1])
img = cv.resize(img, (min,min))
img[img>=225] = 0

M,N = img.shape
fourier_image = np.fft.fft2(img)
u = np.array(range(0,M))
v = np.array(range(0,N))
idx = np.where(u>(M/2))
u[idx] = u[idx]-M
idy = np.where(v>N/2)
v[idy] = v[idy]-N
[V,U] = np.meshgrid(v,u)
D = (U**2 + V**2)**(1/2)

#cutoff 40
cutoff = [50, 40, 20, 10]
H = 1 - np.exp(((-1)*(D**2))/(2*((cutoff[1])**2)))
G = H * fourier_image
imback = np.fft.ifft2(G)
imback = np.uint8(np.real(imback))

H1 = 1 - np.exp(((-1)*(D**2))/(2*((cutoff[2])**2)))
G1 = H * fourier_image
imback1 = np.fft.ifft2(G1)
imback1 = np.uint8(np.real(imback1))

H2 = 1 - np.exp(((-1)*(D**2))/(2*((cutoff[3])**2)))
G2 = H * fourier_image
imback2 = np.fft.ifft2(G2)
imback2 = np.uint8(np.real(imback2))

images =[img, imback, imback1, imback2]
titles= ['Input Image', 'Cutoff = 40', 'Cutoff = 20', 'Cutoff = 10']

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
 
plt.show()