import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/fa76acb163f7eae7b9dff04ff51a2479.jpg'

image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


_, img_thresh_binary = cv2.threshold(src = image, thresh = 100, maxval = 255, type = cv2.THRESH_BINARY)
_, img_thresh_binary_inv = cv2.threshold(src = image, thresh = 100, maxval = 255, type = cv2.THRESH_BINARY_INV)


plt.figure(figsize=[12,12])

plt.subplot(131);
plt.imshow(image, cmap= 'gray')
plt.title('Original Image')

plt.subplot(132);
plt.imshow(img_thresh_binary, cmap= 'gray')
plt.title('Binary Threshold')

plt.subplot(133);
plt.imshow(img_thresh_binary_inv, cmap= 'gray')
plt.title('Binary Inverse Threshold')


plt.show()
