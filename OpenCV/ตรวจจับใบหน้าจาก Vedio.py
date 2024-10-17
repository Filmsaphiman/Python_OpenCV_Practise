import cv2

cap = cv2.VideoCapture("D:\Python\OpenCVimg\Image\LiSA_Gurenge.mp4")

# อ่านไฟล์ CascadeClassifier
face = cv2.CascadeClassifier("D:\Python\Filed\haarcascade_frontalface_default.xml")

while (cap.isOpened()):
    check , frame = cap.read()
    if check == True :
        grayImg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # แปลง frame เป็น gray scale
        face_detect = face.detectMultiScale(grayImg,1.5,2)

        for (x,y,w,h) in face_detect:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=5)
            cv2.imshow("Output",frame)

        if cv2.waitKey(50) & 0xFF == ord("e"):
            break
    else :
        break
cap.release()
cv2.destroyAllWindows()
