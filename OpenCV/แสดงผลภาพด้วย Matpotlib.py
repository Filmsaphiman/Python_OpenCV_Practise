import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:\Python\OpenCVimg\Image\Dog.jpg")
cv2.imshow("Output",img)

plt.imshow(img)
plt.show()