import cv2
from skimage.filters import frangi
import numpy as np
import matplotlib.pyplot as plt
path= r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/project/leaf.png'

image = cv2.imread(path, 0)

ridges = frangi(image)

plt.subplot(221), plt.imshow(image, cmap = "gray")
plt.title ('Original Image')
plt.subplot(222), plt.imshow(ridges, cmap = "gray")
plt.title ('Ridge Detected Image')