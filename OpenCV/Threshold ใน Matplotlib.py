import cv2
import matplotlib.pyplot as plt

img = cv2.imread("D:\Python\OpenCVimg\Image\GradientBG.jpg")
GradientBG = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh,th1 = cv2.threshold(GradientBG,128,255,cv2.THRESH_BINARY)
thresh,th2 = cv2.threshold(GradientBG,128,255,cv2.THRESH_BINARY_INV)
thresh,th3 = cv2.threshold(GradientBG,128,255,cv2.THRESH_TRUNC)
thresh,th4 = cv2.threshold(GradientBG,128,255,cv2.THRESH_TOZERO)
thresh,th5 = cv2.threshold(GradientBG,128,255,cv2.THRESH_TOZERO_INV)

images = [GradientBG,th1,th2,th3,th4,th5]
titles = ["Original","BINARY","BINARY_INV","TRUNC","TOZERO","TOZERO_INV"]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.title(titles[i])
    plt.imshow(images[i],cmap="gray")
    plt.xticks([]),plt.yticks([])
plt.show()

