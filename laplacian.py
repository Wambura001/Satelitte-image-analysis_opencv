import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/project/waterfall.jpeg'
image = cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

laplacian = cv2.Laplacian(image, cv2.CV_64F, ksize=3)
laplacian_abs = cv2.convertScaleAbs(laplacian)

kernel_4 = np.array([[0, -1, 0],[-1, 4, -1],[0, -1, 0]])
kernel_8 = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]])

laplacian_4 =cv2.filter2D(image, cv2.CV_64F, kernel_4)
laplacian_8 =cv2.filter2D(image, cv2.CV_64F, kernel_8)

laplacian_4_abs = cv2.convertScaleAbs(laplacian_4)
laplacian_8_abs = cv2.convertScaleAbs(laplacian_8)

plt.figure(figsize=(20,15))

plt.subplot(221)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.axis('Off')

plt.subplot(222)
plt.imshow(laplacian_abs, cmap='gray')
plt.title('OpenCV Laplacian')
plt.axis('Off')

plt.subplot(223)
plt.imshow(laplacian_4_abs , cmap='gray')
plt.title('Custom Laplacian (4 neighbours)')
plt.axis('Off')

plt.subplot(224)
plt.imshow(laplacian_8_abs, cmap='gray')
plt.title('Custom Laplacian (8 neighbours)')
plt.axis('Off')

plt.show()