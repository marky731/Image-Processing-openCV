import cv2
import numpy as np

def get_limits(color):
    c = np.array([[color]], dtype=np.uint8) #here insert the bgr values which you want to convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] -10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8) # 8 bit unsigned integer date type 
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit




def modify_image_size(image, xImage=None, yImage=None, percent=1):
    if xImage == None and yImage == None: 
        print("x and y is changed") 
        x,y, channel = image.shape
        x = int(x*percent)
        y = int(y*percent)
        print("x and y is changed")
    else:
        y = int(yImage*percent)
        x = int(xImage*percent)
        print("2 2 2 2 ")


    image = cv2.resize(image, (y,x), interpolation=cv2.INTER_LINEAR)
    print("modify_size function has executed")
    return image

def reduce_image_size(image, percent):
     x,y,channels = image.shape

     x = int(x*percent)
     y = int(y*percent)

     image = cv2.resize(image, (y,x), interpolation=cv2.INTER_LINEAR)
     print("reduce size funciton has executed  ")
     return image



def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver
