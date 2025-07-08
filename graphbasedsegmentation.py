#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 17:17:46 2025

@author: leon
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import felzenszwalb 

path= r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/annotation/sports.jpeg'
image = cv2.imread(path) 
image= cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

segments = felzenszwalb(image, scale=100, sigma=0.5, min_size=50)

plt.subplot(121), plt.imshow(image),plt.title('Original Image'), plt.axis('off')
plt.subplot(122),plt.imshow(segments, cmap='hsv'), plt.title('Felzenszwalb Segmentation')
plt.axis('off')
plt.show()