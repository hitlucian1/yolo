from ultralytics import YOLO
import cv2
model=YOLO('yolov8x.pt')
results=model('../images/3.jpg',show=True)
cv2.waitKey(0)