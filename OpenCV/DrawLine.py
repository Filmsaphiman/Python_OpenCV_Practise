import cv2
import numpy as np

img = np.zeros([400,400,3])

point = []

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN :
        cv2.circle(img,(x,y),10,(225,0,0),5)
        point.append((x,y))
        print(point)
        if len(point) >= 2 :
            cv2.line(img,point[-2],point[-1],(0,0,225),2)
    cv2.imshow("Output", img) # เป็น imshow ที่แสดงหน้าต่างที่มีวงกลมอยู่ด้วย เป็นคำสั่ง imshow ที่เป็นส่วนหนึ่งของ def ถ้าไม่มี imshow บรรทัดนี้ จะไม่มีหน้าต่างที่แสดงผลวงกลมและการลากเส้น

cv2.imshow("Output",img) # ถ้าไม่มีบรรทัดนี้จะเกิด error ที่บรรทัด 19 เพราะไม่มี Window ชื่อ "Output" ใน function setMouseCallback  : ก็มันบอกมางี้ มั้งนะ ตามความเข้าใจอ่ะ 55555
# imshow บรรทัดนี้มีเพื่อให้บรรทัด 19 รู้ว่ามี window "Output" อยู่  เพื่อจะสามารถเรียกใช้งาน setMouseCallback ได้
cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey()
cv2.destroyAllWindow()
