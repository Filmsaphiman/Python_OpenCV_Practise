import cv2

cap = cv2.VideoCapture(0)

while(cap.isOpened()):
# จับภาพแบบ frame ต่อ frame
    ret, frame = cap.read()
    if ret == True:
        # แสดงผลของ frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break

# แสดงภาพจากกล้อง
cap.release()
cv2.destroyAllWindows()
