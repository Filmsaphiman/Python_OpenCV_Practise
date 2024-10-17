import cv2
def display(value):
    pass

cv2.namedWindow("Output")
cv2.createTrackbar("Value","Output",128,255,display)

while True:
    grayImg = cv2.imread("D:\Python\OpenCVimg\Image\GradientBG.jpg",0)
    thresh_value = cv2.getTrackbarPos("Value","Output")
    thresh,result = cv2.threshold(grayImg,thresh_value,255,cv2.THRESH_BINARY)
    if cv2.waitKey(50) & 0xFF == ord("e"):
        break
    cv2.imshow("Output",result)

cv2.destroyAllWindows()