import ultralytics 


model = ultralytics.YOLO("2023.12.23/shape_detection.pt") 

results = model(source=0, show=True, conf=0.4)