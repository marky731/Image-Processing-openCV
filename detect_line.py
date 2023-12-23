import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for white color
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([255, 30, 255])
    white_mask = cv2.inRange(hsv, lower_white, upper_white)
    white_result = cv2.bitwise_and(img, img, mask=white_mask)

    # Define the lower and upper bounds for red color
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    red_mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([160, 100, 100])
    upper_red = np.array([180, 255, 255])
    red_mask2 = cv2.inRange(hsv, lower_red, upper_red)
    red_mask = red_mask1 + red_mask2
    
    red_result = cv2.bitwise_and(img, img, mask=red_mask)

    # Define the lower and upper bounds for blue color
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    blue_result = cv2.bitwise_and(img, img, mask=blue_mask)

    # white and red areas remain in the result, other colors turn into black
    result = cv2.addWeighted(white_result, 1, red_result, 1, 0)

    # Invert the grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # convert the bits (0->1, 1->0)
    inverted_image = cv2.bitwise_not(gray)

    # take the black areas
    ret, black_line = cv2.threshold(inverted_image, 220, 255, cv2.THRESH_BINARY)

    # display the black area if you want
    cv2.imshow("black_line", black_line)

    # find the countour of black area
    contour_blackline, _ = cv2.findContours(black_line.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # draw the contour of black area
    result = cv2.drawContours(result, contour_blackline, -1, (0,255,0), 2)

    # Display the result
    cv2.imshow("Result", result)

    key = cv2.waitKey(1)
    if key == ord("q"):
        cv2.destroyAllWindows()
        break

