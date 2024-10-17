import cv2
cap = cv2.VideoCapture("D:\Python\OpenCVimg\Image\LiSA _Gurenge.mp4")

while (cap.isOpened()):

    check , frame = cap.read()
    if check == True:
        print(cap.isOpened())
        print(cap.read())
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break

cap.release()
cv2.destroyAllWindows()
