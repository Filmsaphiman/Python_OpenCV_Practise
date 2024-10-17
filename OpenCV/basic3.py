import cv2
import datetime

cap = cv2.VideoCapture("D:\Python\OpenCVimg\Image\LiSA _Gurenge.mp4")

while(cap.isOpened()) :
    check , frame = cap.read()
    cv2.resize(frame,(200,200))
    if check == True :
        currentData = str(datetime.datetime.now())
        cv2.putText(frame, currentData,(10,80),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255))
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()