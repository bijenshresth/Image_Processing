import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_1 = cv.imread('fractured.png', 0)

gamma = 2
img_2 = np.power(img_1, gamma)

gamma = 3
img_3 = np.power(img_1, gamma)

gamma = 4
img_4 = np.power(img_1, gamma)
images = [img_1, img_2, img_3, img_4]
titles = ['Original Image', 'gamma = 2', 'gamma = 3', 'gamma = 4']
for i in range(4):
   plt.subplot(2, 2, i+1)
   plt.imshow(images[i], 'gray')
   plt.title(titles[i])
   plt.xticks([])
   plt.yticks([])
plt.show()
