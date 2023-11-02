import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    y, x, _ = hsv_frame.shape # it gives the height (y-axis) first
    center = (int(x/2), int(y/2))
    cX = int(x/2)
    cY = int(y/2)

    cv2.circle(frame, center, 5, (0,255,177), 2)
    pixel_center = hsv_frame[cY,cX]

    cv2.imshow("pixel_center", pixel_center)
    print("center: ", pixel_center)

    color = "Undefined"
    text_color = (0,0,0)

    hue_value, saturation, value = pixel_center
    if saturation <90 and value < 80:
        color="BLACK"
        text_color = (0,0,0)
    elif saturation < 59 and value > 210:
        color="WHITE"
        text_color = (255,255,255)
    else:
        if hue_value < 5:
            color="RED"
            text_color = (0,0,255)
        elif hue_value < 22:
            color="ORANGE"
            text_color = (11,111,255)
        elif hue_value < 33:
            color="YELLOW"
            text_color = (0,255,255)
        elif hue_value < 78:
            color="GREEN"
            text_color = (0,255,0)
        elif hue_value < 131:
            color="BLUE"
            text_color = (255,0,0)
        elif hue_value < 167:
            color="PURPLE"
            text_color = (255,0,255)
        else :
            color = "RED"
            text_color = (0,0,255)

    cv2.putText(frame, color, (22,33), cv2.FONT_HERSHEY_COMPLEX, 0.9, text_color, 3)

    cv2.imshow("window", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows
print("Program bitti kardeşim bak işine ! ")