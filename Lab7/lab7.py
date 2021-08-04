import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("walk.jpg", 0)

img1 = cv.resize(img, (350, 350))
hist1 = cv.calcHist(img1, [0], None, [256], [0, 256])

equ = cv.equalizeHist(img1)
histequ = cv.calcHist(equ, [0], None, [256], [0, 256])

final = np.hstack((img1, equ))
cv.imshow("final image", final)

hists = [hist1, histequ]
titles = ['Low Contrast Image', 'Histogram Equalized Image']

for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.plot(hists[i])
    plt.title(titles[i])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()