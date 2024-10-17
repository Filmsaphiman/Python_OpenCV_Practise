import cv2
import numpy

while True:
    img = cv2.imread("D:\Python\OpenCVimg\Image\LookKaw.png")
    img = cv2.resize(img,(400,400))

    lower = numpy.array([0, 53, 3])
    upper = numpy.array([186, 225, 102])

    mask = cv2.inRange(img,lower,upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    if cv2.waitKey(0) & 0xFF == ord("e"):
        break

    cv2.imshow("Original", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()