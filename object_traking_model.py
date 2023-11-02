import cv2
import time
import threading

from ultralytics import YOLO
import math 



class Camera:
    def __init__(self, model_file, video_port):
        self.model_file = model_file
        self.video_port = video_port
        self.active = True
        self.isCameraActive = False
        self.camera = cv2.VideoCapture(self.video_port)
        self.Frame = None
        self.cameraThread = threading.Thread(target=self.getFrame)

        self.model = YOLO(self.model_file) # its safer to use self.modelFile instead of model_file 
        self.cameraThread.start()

        while not self.isCameraActive:
            self.isCameraActive = self.camera.isOpened()


    def openCamera(self):
        return cv2.VideoCapture(self.video_port)

    def getFrame(self):
        while self.active:
            ret, frame = self.camera.read()
            if ret:
                self.Frame = frame
                self.isCameraActive = ret
                # print("frame has setted!  ")
            else:
                print("getFrame() error")
                # self.active = False  # Stop the thread when there's an error

        self.camera.release()

    def return_frame(self):
        return self.Frame
    
    def detectObject(self, frame):
        results = self.model(frame, stream=True) # gives an yolov8 objects
        return results


width = 640
higth = 640
cv2.namedWindow('Currentframe', cv2.WINDOW_NORMAL)  # Create a resizable window
# cv2.resizeWindow('Currentframe', width, higth)  # Set the width and height


the_camera = Camera('./unicornModel.pt', 0)

pTime = 0
cTime = 0

while True:
    if the_camera.isCameraActive:
        try:
                frame =  cv2.resize(the_camera.return_frame(), (640,640))
                # frame =  the_camera.return_frame()

                centerX, centerY = width//2, higth//2

                position = the_camera.detectObject(frame)

                for p in position:
                    boxes_ = p.boxes

                    for box in boxes_:
                        x1, y1, x2, y2 = box.xyxy[0]
                        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                        confidence = math.ceil((box.conf[0] * 100)) / 100
                        print(confidence)

                        if confidence >= 0.8 :
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                            cv2.putText(frame, str(confidence), (x1,y1), cv2.FONT_HERSHEY_COMPLEX, 1, (171,171,1), 1)

                            x_centeBox = (x1+x2)/2
                            y_centerBox = (y1+y2)/2

                            cor_x = x_centeBox - centerX
                            cor_y = centerY - y_centerBox
                            text = f"X: {cor_x}, Y: {cor_y}"

                            cv2.putText(frame, text, (x1, y2+10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,0), 1)
        
                cTime = time.time()
                fps = 1/(cTime - pTime)
                pTime = cTime
                cv2.putText(frame, str(int(fps)),(10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255,0,255), 3)
                cv2.imshow("Currentframe", frame)
                key = cv2.waitKey(1)
                if key == ord('q'):
                    cv2.destroyAllWindows()
                    the_camera.active = False
                    break
            
        except Exception as ee:
            print('Error my baby: ', ee)
