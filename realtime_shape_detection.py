import cv2
import numpy as np
from Functions_For_ImageProcessing import modify_image_size # self made functions 



def nothing(x):
    # any operation
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Mask")
cv2.createTrackbar("L-H", "Mask", 0, 180, nothing) 
cv2.createTrackbar("L-S", "Mask", 66, 255, nothing)
cv2.createTrackbar("L-V", "Mask", 134, 255, nothing)
cv2.createTrackbar("U-H", "Mask", 180, 180, nothing)
cv2.createTrackbar("U-S", "Mask", 255, 255, nothing)
cv2.createTrackbar("U-V", "Mask", 243, 255, nothing)

font = cv2.FONT_HERSHEY_COMPLEX

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H", "Mask") 
    l_s = cv2.getTrackbarPos("L-S", "Mask")
    l_v = cv2.getTrackbarPos("L-V", "Mask") # lower limits of hsv values
    u_h = cv2.getTrackbarPos("U-H", "Mask") # upper limits of hsc values
    u_s = cv2.getTrackbarPos("U-S", "Mask")
    u_v = cv2.getTrackbarPos("U-V", "Mask")

    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower_red, upper_red) # change the pixels which have color between upper red and lower red to white
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)

    # Contours detection
    if int(cv2.__version__[0]) > 3:
        # Opencv 4.x.xq
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    else:
        # Opencv 3.x.x
        _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.008*cv2.arcLength(cnt, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]

        if area > 1000:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)

            if len(approx) == 3:
                cv2.putText(frame, "Triangle", (x, y), font, 1, (0,255,0))
                print("3")
            elif len(approx) == 4:
                cv2.putText(frame, "Rectangle", (x, y), font, 1, (255,0,0))
                print("4")
            elif len(approx) == 5:
                cv2.putText(frame, "Pentagon", (x, y), font, 1, (0,0,255))
                print("5")
            elif len(approx) == 6:
                cv2.putText(frame, "Hexagon", (x, y), font, 1, (0,255,255))
                print("5")
            elif 7 < len(approx) < 15:
                cv2.putText(frame, "Ellipse", (x, y), font, 1, (255, 0, 255))
                print("6-15")
            else:
                cv2.putText(frame, "Circle", (x, y), font, 1, (255,255,0))
                print("circle")


    frame = modify_image_size(frame,percent=0.8)
    mask = modify_image_size(mask,percent=0.8)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
