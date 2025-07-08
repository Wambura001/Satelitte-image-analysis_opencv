import cv2
import numpy as np
import matplotlib.pyplot as plt

path= r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/project/cheetah.jpg'
image = cv2.imread(path, 0)

params = cv2.SimpleBlobDetector_Params()

params.filterByArea = True
params.minArea = 100
params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(image)

image_with_keypoints = cv2.drawKeypoints(image, keypoints, np.array([]),
(0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.subplot(221), plt.imshow(image, cmap = "gray"),plt.title ('Original Image')
plt.subplot(222), plt.imshow(cv2.cvtColor(image_with_keypoints, cv2.COLOR_BGR2RGB)),
plt.title ('Blobs Detected Image')