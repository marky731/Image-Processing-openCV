import cv2 as cv 
import numpy as np

videoCapture = cv.VideoCapture(0)
prevCircle = None
dist = lambda x1,y1,x2,y2: (x1-x2)**2+(y1-y2)**2

while True:
    ret, frame = videoCapture.read()
    if not ret: break

    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurFrame = cv.GaussianBlur(grayFrame, (35,35), 0) # (35,35) seems like the optimal value for now
    # cannyFrame = cv.Canny(blurFrame, 110, 130)
    # cv.imshow("blurr", blurFrame)
    # cv.imshow("canny", cannyFrame)

    contours, hierarchy = cv.findContours(grayFrame, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    print(contours)

    cv.drawContours(grayFrame,contours,-1,(0,255,0), 2)
    cv.imshow("contorus",grayFrame)


    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=75, maxRadius=400)

    ## draw circle currently
    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosenCircle = None # the one with the longest distance with prev
        for i in circles[0, :]:
            if chosenCircle is None: chosenCircle = i
            if prevCircle is not None:
                if dist(chosenCircle[0],chosenCircle[1],prevCircle[0],prevCircle[1]) <= dist(i[0],i[1],prevCircle[0],prevCircle[1]):
                    chosenCircle =  i # if i has longer distance, assigne i to chosenCircle
        cv.circle(frame, (chosenCircle[0], chosenCircle[1]), 1, (9,100,190), 5)
        cv.circle(frame, (chosenCircle[0], chosenCircle[1]), chosenCircle[2], (255,0,0),3)
        prevCircle = chosenCircle

    cv.imshow("camera", frame)

    if cv.waitKey(1) == ord('q'): break

videoCapture.release()
cv.destroyAllWindows()








# import cv2 as cv
# import numpy as np

from FunctionsForImageProcessing import modify_image_size


# videoCapture = cv.VideoCapture(0)
# prevCircle = None
# dist = lambda x1, y1, x2, y2: (x1 - x2) ** 2 + (y1 - y2) ** 2

# while True:
#     ret, frame = videoCapture.read()
#     if not ret:
#         break

#     grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     _, thresh = cv.threshold(grayFrame,230,255,cv.THRESH_BINARY_INV)
#     canny = cv.Canny(thresh, 244, 255)
#     x, y = canny.shape
#     canny = reduce_image_size(canny, x, y, percent=0.8)
#     frame = reduce_image_size(frame, x, y, percent=0.8)
#     cv.imshow("canny", canny)
#     # blurFrame = cv.GaussianBlur(grayFrame, (35, 35), 0)
#     frame_copy = frame.copy()
    
#     # Find contours on the grayscale image
#     contours, hierarchy = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
#     print(contours)

#     contours_frame = canny.copy()

#     # Draw the contours on the original frame
#     cv.drawContours(contours_frame, contours, -1, (0, 255, 0), 2)
    
#     # cv.imshow("blurr", blurFrame)
#     cv.imshow("contours", contours_frame)  # Display the frame with contours

#     circles = cv.HoughCircles(canny, cv.HOUGH_GRADIENT, 1.2, 100, param1=100, param2=30, minRadius=75, maxRadius=400)

#     if circles is not None:
#         circles = np.uint16(np.around(circles))
#         chosen = None
#         for i in circles[0, :]:
#             if chosen is None:
#                 chosen = i
#             if prevCircle is not None:
#                 if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
#                     chosen = i
#         cv.circle(frame, (chosen[0], chosen[1]), 1, (9, 100, 190), 5)
#         cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (255, 0, 0), 3)
#         prevCircle = chosen  ## guy from youtube

#     # if circles is not None:
#     #     circles = np.uint16(np.around(circles))
#     #     for circle in circles[0, :]:
#     #         center_x, center_y = circle[0], circle[1]
#     #         radius = circle[2]
#     #         cv.circle(frame, (center_x, center_y), radius, (0, 255, 0), 2)


#     cv.imshow("camera", frame)

#     if cv.waitKey(1) == ord('q'):
#         break

# videoCapture.release()
# cv.destroyAllWindows()


