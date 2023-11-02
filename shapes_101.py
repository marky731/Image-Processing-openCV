import cv2 
import numpy as np

font = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread("/Users/mac/Desktop/Programming/Python/Image_Processing/shape_detecting/shapes.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY) # thresh is the value above which we consider it to be white

img_2 = img.copy()
contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("image", img_2) 


cv2.drawContours(img, contours, -1, (255,255,0), 2)

print("len(contours): ", len(contours))

sortedCon = sorted(contours, key = cv2.contourArea, reverse=True)

for cnt in sortedCon:

    arcLength = cv2.arcLength(cnt, True)
    print("arcLength: ", arcLength)
    cnt = cv2.approxPolyDP(cnt, 0.008*cv2.arcLength(cnt, True), True)
    print("cnt: ", cnt)
    cv2.drawContours(img_2, [cnt], -1, (0,255,0),3 )
    x = cnt.ravel()[0]
    y = cnt.ravel()[1]
    if len(cnt) == 3:
        cv2.putText(img_2, "Triangle", (x, y), font, 1, (0))
        print("3")
    elif len(cnt) == 4:
        cv2.putText(img_2, "Rectangle", (x, y), font, 1, (0))
        print("4")
    elif len(cnt) == 5:
        cv2.putText(img_2, "Pentagon", (x, y), font, 1, (0))
        print("5")
    elif len(cnt) == 6:
        cv2.putText(img_2, "Hexagon", (x, y), font, 1, (0))
        print("5")
    elif 7 < len(cnt) < 15:
        cv2.putText(img_2, "Ellipse", (x, y), font, 1, (0))
        print("6-15")
    else:
        cv2.putText(img_2, "Circle", (x, y), font, 1, (0))
        print("circle")



cv2.imshow("contours", img) # check the contours which are found by cv2.findContour()
cv2.imshow("Threshold", threshold)
cv2.imshow("result", img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
