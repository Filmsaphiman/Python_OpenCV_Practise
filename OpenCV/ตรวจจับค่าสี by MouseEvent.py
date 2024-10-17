import cv2
img = cv2.imread("D:\Python\OpenCVimg\Image\RGB.png")

def clickMouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN :
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]

        cv2.putText(img,(str(blue)+","+str(green)+","+str(red)),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,225))
        cv2.imshow("Output",img)

cv2.imshow("Output",img)
cv2.setMouseCallback("Output",clickMouse)
cv2.waitKey()
cv2.destroyAllWindow()