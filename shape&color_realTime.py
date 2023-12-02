import cv2
from Functions_For_ImageProcessing import get_limits, modify_image_size
import threading
import time
import sys
url = "https://192.168.1.103:8080/video"

yellow = [0,255,255]
purple = [255,0,255]
green = [0,255,0]
blue = [255,0,0]

font = cv2.FONT_HERSHEY_COMPLEX

color = yellow
isColorChanged = True

def nothing(x):
    pass # empty function

cv2.namedWindow("yellow=0,   purple=1,  green=2,  blue=3")
cv2.createTrackbar("Color Index", "yellow=0,   purple=1,  green=2,  blue=3", 0, 4, nothing)

img = cv2.imread("/Users/mac/Desktop/Programming/Python/image_processing_2/shapes.jpg")
# cap = cv2.VideoCapture(url)
# ret, img = cap.read()


while True:

    colorPrevious = color

    color_index = cv2.getTrackbarPos("Color Index", "yellow=0,   purple=1,  green=2,  blue=3")
    int(color_index)

    # if isColorChanged = 
    if color_index == 0:
        color = yellow
    elif color_index == 1:
        color = purple
    elif color_index == 2:
        color = green
    elif color_index == 3:
        color = blue
    
    if colorPrevious != color:
        img = cv2.imread("/Users/mac/Desktop/Programming/Python/image_processing_2/shapes.jpg")
        # ret, img = cap.read()



        lowerLimit, upperLimit = get_limits(color)

        hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        x_mask, y_mask = mask.shape
        x_frame, y_frame, channel = img.shape

        # mask = modify_image_size(mask, xImage=x_mask, yImage=y_mask, percent=0.75)    # # this is optional since it just adjusts the size of the output image
        # img = modify_image_size(img, xImage=x_frame, yImage=y_frame, percent=0.75)    # # this is optional since it just adjusts the size of the output image

        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # external = 外轮廓
        cv2.drawContours(img, contours, -1, (255,0,255), 2)


    ####################################################################### (shape detection part)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, threshold = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY) # thresh is the value above which we consider it to be white

        contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        # cv2.drawContours(img, contours, -1, (255,255,0), 2)

        print("len(contours): ", len(contours))

        sortedCon = sorted(contours, key = cv2.contourArea, reverse=True)

        for cnt in sortedCon:

            arcLength = cv2.arcLength(cnt, True)
            print("arcLength: ", arcLength)
            cnt = cv2.approxPolyDP(cnt, 0.008*cv2.arcLength(cnt, True), True)
            print("cnt: ", cnt)
            # cv2.drawContours(img, [cnt], -1, (0,255,0),3 )
            x = cnt.ravel()[0]
            y = cnt.ravel()[1]
            if len(cnt) == 3:
                cv2.putText(img, "Triangle", (x, y), font, 1, (0))
                print("3")
            elif len(cnt) == 4:
                cv2.putText(img, "Rectangle", (x, y), font, 1, (0))
                print("4")
            elif len(cnt) == 5:
                cv2.putText(img, "Pentagon", (x, y), font, 1, (0))
                print("5")
            elif len(cnt) == 6:
                cv2.putText(img, "Hexagon", (x, y), font, 1, (0))
                print("5")
            elif 7 < len(cnt) < 15:
                cv2.putText(img, "Ellipse", (x, y), font, 1, (0))
                print("6-15")
            else:
                cv2.putText(img, "Circle", (x, y), font, 1, (0))
        #         print("circle")

    cv2.imshow("yellow=0,   purple=1,  green=2,  blue=3", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        sys.exit()



                


