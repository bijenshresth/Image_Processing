# Log Transformation of an image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("dft.png")
c = 255/np.log(1+np.max(image))
log_image = c*(np.log(image + 1))
log_image = np.array(log_image, dtype=np.uint8)
images = [image, log_image]
titles = ['Original Image', 'Log Transformed Image']
for i in range (2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
