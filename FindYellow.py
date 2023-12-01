import cv2
from Functions_For_ImageProcessing import get_limits, modify_image_size

yellow = [0,255,255]
red = [0,0,255]
purple = [255,0,255]
green = [0,255,0]
blue = [255,0,0]


# color = str(input("Which color you want to detect? (yellow, red, purple, green, blue)"))

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    lowerLimit, upperLimit = get_limits(yellow)

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    x_mask, y_mask = mask.shape
    x_frame, y_frame, channel = frame.shape

    mask = modify_image_size(mask, xImage=x_mask, yImage=y_mask, percent=0.75)    # # this is optional since it just adjusts the size of the output image
    frame = modify_image_size(frame, xImage=x_frame, yImage=y_frame, percent=0.75)    # # this is optional since it just adjusts the size of the output image

    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE) # external = 外轮廓
    cv2.drawContours(frame, contours, -1, (255,0,255), 2)


    # cv2.imshow("mask", mask)
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
