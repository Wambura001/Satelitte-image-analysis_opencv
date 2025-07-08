import cv2
import numpy as np
import matplotlib.pyplot as plt

path= r'/Users/leon/Documents/SPRING_25_SOPHOMORE/COMPUTER VISION::ZUBAER/project/waterfall.jpeg'
image= cv2.imread(path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

sobel_x= cv2.Sobel(image, cv2.CV_64F, 0,1, ksize=3)
sobel_y= cv2.Sobel(image, cv2.CV_64F, 0,1, ksize=3)

abs_sobel_x= cv2.convertScaleAbs(sobel_x)
abs_sobel_y= cv2.convertScaleAbs(sobel_y)

sobel_combined = np.sqrt(sobel_x**2 + sobel_y**2)
sobel_combined = np.uint8(np.clip(sobel_combined,0, 255))

plt.figure(figsize=(20, 15))

plt.subplot(221)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("Off")

plt.subplot(222)
plt.imshow(abs_sobel_x , cmap="gray")
plt.title(" Sobel X ")
plt.axis("Off")

plt.subplot(223)
plt.imshow(abs_sobel_y , cmap="gray")
plt.title(" Sobel Y")
plt.axis("Off")

plt.subplot(224)
plt.imshow(sobel_combined , cmap="gray")
plt.title(" Sobel Combined")
plt.axis("Off")

plt.show()