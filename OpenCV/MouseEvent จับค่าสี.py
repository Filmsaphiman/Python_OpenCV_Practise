import cv2
import numpy
img = cv2.imread("D:\Python\OpenCVimg\Image\L 6.jpg")
img = cv2.resize(img,(700,700))
def ClickMouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        Blue = img[y,x,0]
        Green = img[y,x,1]
        Red = img[y,x,2]

        text = str(Blue)+","+str(Green)+","+str(Red)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,225),cv2.LINE_4)
        cv2.imshow("Output", img)

        imgcolor = numpy.zeros([300,300,3],numpy.uint8)
        imgcolor[:] = [Blue,Green,Red]
        cv2.imshow("Result",imgcolor)


cv2.imshow("Output",img)
cv2.setMouseCallback("Output",ClickMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()