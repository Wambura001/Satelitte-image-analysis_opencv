import cv2
import matplotlib.pyplot as plt

path=r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/project/waterfall.jpeg'
image=cv2.imread(path, 0)

edges = cv2.Canny(image, threshold1=50, threshold2=150)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1,2,2)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')
plt.show()
