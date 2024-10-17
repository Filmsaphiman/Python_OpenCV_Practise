import cv2
import numpy as np

cv2.namedWindow("Color Trackbar")
def display(value):
    print(value)

cv2.createTrackbar("threshold_value","Color Trackbar",0,255,display)
cv2.createTrackbar("B","Color Trackbar",0,255,display)
cv2.createTrackbar("G","Color Trackbar",0,255,display)
cv2.createTrackbar("R","Color Trackbar",0,255,display)

while True:
    img = cv2.imread("D:\Python\OpenCVimg\Image\GradientBG.jpg")
    cv2.imshow("Color Trackbar",img)

    thresh_value = cv2.getTrackbarPos("threshold_value","Color Trackbar")
    thresh, result = cv2.threshold(img, thresh_value,255,cv2.THRESH_BINARY)

    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

    cv2.imshow("Color Trackbar", result)

    Blue = cv2.getTrackbarPos("B", "Color Trackbar")
    Green = cv2.getTrackbarPos("G", "Color Trackbar")
    Red = cv2.getTrackbarPos("R", "Color Trackbar")
    img[:] = [Blue, Green, Red]

cv2.destroyAllWindows()
