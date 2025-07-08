import cv2
import numpy as np
import matplotlib.pyplot as plt

path= r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/project/chessboard.png'
image = cv2.imread(path)

plt.subplot(121),plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)),
plt.title('Original Image'), plt.axis('off')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray) 

dst = cv2.cornerHarris(gray, blockSize = 2, ksize = 3, k = 0.04)
dst = cv2.dilate(dst, None) 
image[dst > 0.01 * dst.max()] = [0, 0, 255] 

plt.subplot(122),plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Harris Corners'), plt.axis('off')
plt.show()