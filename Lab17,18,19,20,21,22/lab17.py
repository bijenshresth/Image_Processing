#Implementation of Ideal Low Pass Filter 

import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv
from numpy.lib.histograms import _get_outer_edges

img = cv.imread('smile.jpg',0)
min = np.minimum(img.shape[0],img.shape[1])
img = cv.resize(img,(min,min))
img[img>=225]=0

M,N = img.shape
fourier_image = np.fft.fft2(img)
u = np.array(range(0,M))
v = np.array(range(0,N))
idx = np.where(u>(M/2))
u[idx] = u[idx]-M
idy = np.where(v>N/2)
v[idy]=v[idy]-N
[V,U] = np.meshgrid(v,u)
D = (U**2 + V**2)**(1/2)
#cutoff = 40
cutoff = [50,40,20,10]
H = (D<=40)
G = H*fourier_image
imback = np.fft.ifft2(G)
imback = np.uint8(np.real(imback))
imback[imback>=225]=0
H1=(D<=20)
G1 = H1*fourier_image
imback1= np.fft.ifft2(G1)
imback1 = np.uint8(np.real(imback1))
imback1[imback1>=225]=0

fshift = np.fft.fftshift(fourier_image)
magnitude_spectrum = 20 *np.log(np.abs(fshift))

images =[img,imback,imback1]
titles= ['Input Image','Cutoff = 40','Cutoff = 20']

for i in range(3):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
 
plt.show()

