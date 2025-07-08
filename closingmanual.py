import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/morphological.png'
image = cv2.imread(path)

_, binary = cv2.threshold(image, 127,255, cv2.THRESH_BINARY)

kernel = np.ones((5,5), np.uint8)
dialated = cv2.dilate(binary, kernel, iterations=1)

closing_manual= cv2.erode(dialated, kernel, iterations=1)

cv2.imshow('Original Binary Image', binary)
cv2.imshow('Dialated Image', dialated)
cv2.imshow('Morphological closing manual', closing_manual)
cv2.waitKey(0)
cv2.destroyAllWindows()