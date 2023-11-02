import cv2
from FunctionsForImageProcessing import get_limits, modify_image_size
import threading
import time
import sys


yellow = [0,255,255]
purple = [255,0,255]
green = [0,255,0]
blue = [255,0,0]

print(get_limits(yellow))
print(get_limits(blue))
print(get_limits(purple))
print(get_limits(green))

def nothing(x):
    pass # empty function

cv2.namedWindow("yellow=0,   purple=1,  green=2,  blue=3")
cv2.createTrackbar("Color Index", "yellow=0,   purple=1,  green=2,  blue=3", 0, 4, nothing)

def detec_color(color: list):
    while True:
        
        color_index = cv2.getTrackbarPos("Color Index", "yellow=0,   purple=1,  green=2,  blue=3")
        int(color_index)
        print(color_index)
        if color_index == 0:
            color = yellow
        elif color_index == 1:
            color = purple
        elif color_index == 2:
            color = green
        elif color_index == 3:
            color = blue

        ret, frame = cap.read()

        lowerLimit, upperLimit = get_limits(color)

        hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

        x_mask, y_mask = mask.shape
        x_frame, y_frame, channel = frame.shape

        mask = modify_image_size(mask, xImage=x_mask, yImage=y_mask, percent=0.75)    # # this is optional since it just adjusts the size of the output image
        frame = modify_image_size(frame, xImage=x_frame, yImage=y_frame, percent=0.75)    # # this is optional since it just adjusts the size of the output image

        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # external = 外轮廓
        cv2.drawContours(frame, contours, -1, (255,0,255), 2)


        # cv2.imshow("mask", mask)
        cv2.imshow("yellow=0,   purple=1,  green=2,  blue=3", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            sys.exit()


cap = cv2.VideoCapture(0)
detec_color(yellow)
            


# while True:
#     colorToDetect = input("yellow: 1,  red: 2, purple: 3, green: 4, blue: 5")



# detec_color(red)



# thread1 = threading.Thread(target=detec_color, args=(red,))
# thread2 = threading.Thread(target=detec_color, args=yellow)
# thread3 = threading.Thread(target=detec_color, args=blue)
# thread4 = threading.Thread(target=detec_color, args=green)


# thread1.start()
# thread2.start()
# thread3.start()
# thread4.start()
