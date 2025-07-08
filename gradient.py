import cv2
import numpy as np
import matplotlib.pyplot as plt

path= r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/morphological.png'
image = cv2.imread(path)

_, binary = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)

gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT,kernel)

cv2.imshow('Original Binary Image', binary)
cv2.imshow('Morphological Gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()