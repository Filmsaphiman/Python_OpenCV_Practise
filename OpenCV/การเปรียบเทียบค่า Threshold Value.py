import cv2
import  matplotlib.pyplot as plt

img = cv2.imread("D:\Python\OpenCVimg\Image\GradientBG.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh_value = [50,100,130,200,230]
plt.subplot(231,xticks=[],yticks=[])
plt.title("Original")
plt.imshow(gray,cmap="gray")

for i in range(len(thresh_value)):
    thresh , result = cv2.threshold(gray,thresh_value[i],255,cv2.THRESH_BINARY)
    plt.subplot(232+i)
    plt.title("%d"%thresh_value[i])
    plt.imshow(result,cmap="gray")

  # plt.xticks=([]),plt.yticks=([]) ใส่แล้ว error คือบ่เป็นคือขะเจ้าเฮ็ดว่ะสู

plt.show()
