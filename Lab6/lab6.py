import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread('girl.png', 0)
img2 = cv.imread('man.png', 0)
img3 = cv.imread('anime.jpg', 0)

hist1 = cv.calcHist([img1], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
hist2 = cv.calcHist([img2], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
hist3 = cv.calcHist([img3], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

images = [img1, img2, img3, hist1, hist2, hist3]
titles = ['Normal Image', 'Low Contrast Image', 'High Contrast Image', '', '', '']
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.title(titles[i])
    if i in range(0,3):
        plt.imshow(images[i])
        plt.xticks([])
    if i in range (3,6):
        plt.plot(images[i])
    plt.yticks([])
plt.show()