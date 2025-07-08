#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 12:37:25 2025

@author: leon
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

path= r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/annotation/sports.jpeg'
img = cv2.imread(path) 
plt.subplot (121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title ('Original Image') 
plt.axis('Off')


Z = img.reshape((-1, 3)) 
Z = np.float32(Z) 

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 4 

_, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
_, labels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

centers = np.uint8(centers)
segmented = centers[labels.flatten()]
segmented_img = segmented.reshape((img.shape))
plt.subplot (122), plt.imshow(cv2.cvtColor(segmented_img, cv2.COLOR_BGR2RGB))
plt.title ('Segmented Image'), plt.axis('Off'), plt.show()