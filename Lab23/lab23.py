# # Salt and Pepper Noise
# import numpy as np
# import random 
# import cv2 as cv
# import matplotlib.pyplot as plt

# def sp_noise(image, prob):
#     output = np.zeros(image.shape, np.uint8)
#     thres = 1 - prob

#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             rdn = random.random()
#             if rdn < prob:
#                 output[i][j] = 0
#             elif rdn > thres:
#                 output[i][j] = 255
#             else:
#                 output[i][j] = image[i][j]
#         return output
    
# image = cv.imread('Capture1234.jpg', 0)
# noise_img = sp_noise(image, 0.05)

# plt.subplot(131), plt.imshow(image, cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(132), plt.imshow(noise_img, cmap = 'gray')
# plt.title('S&P Noise Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(133), plt.hist(noise_img.ravel(), 256, [0, 256])
# plt.title('Histogram'), plt.xticks([]), plt.yticks([])
# plt.show()
import numpy as np
import random
import cv2 
from matplotlib import pyplot as plt

def sp_noise(image,prob):
    output = np.zeros(image.shape,np.uint8)
    thres = 1-prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob :
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]

    return output

image = cv2.imread('Capture1234.jpg',0)
noise_img = sp_noise(image,0.05)
plt.subplot(131),plt.imshow(image,cmap = 'gray')
plt.title('Original Image'),plt.xticks([]),plt.yticks([])

plt.subplot(132),plt.imshow(noise_img,cmap = 'gray')
plt.title('Salt and Pepper Noise'),plt.xticks([]),plt.yticks([])

plt.subplot(133),plt.hist(noise_img.ravel(),256,[0,256])
plt.title('Histogram'),plt.xticks([]),plt.yticks([])

plt.show()
