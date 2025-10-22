import torch
import os
import cv2

MODEL = 'yolov5/runs/train/intruder_detector12/weights/best.pt'

TARGET = 'climbing'

TARGET_ALERT = 0.5

TEST_VIDEO = 'Test_sample.mov'


print("Loading Model")

try:
    model = torch.hub.load('ultralytics/yolov5','custom',path = MODEL)
except Exception as e:
    print(f"Model Loading Failed: {e}")
    exit()

cap = cv2.VideoCapture(TEST_VIDEO)

if not cap.isOpened():
    print(f"Can Not Open Video")
    exit()

print({"Starting Motion Detect"})

while True:
    ret, frame = cap.read()

    results = model(frame)
    detections = results.xyxy[0]

    for det in detections:

        conf = det[4]
        class_id = det[5]
        target_class = model.names[int(class_id)]

        if(target_class == TARGET and conf >= TARGET_ALERT):
            print(f"Climbing Detected")

            video_time_msec = cap.get(cv2.CAP_PROP_POS_MSEC)

            total_seconds = int(video_time_msec / 1000)
            minutes = total_seconds // 60
            seconds = total_seconds % 60
                
            print(f"---'{TARGET}' Detected [time 시간: {minutes:02d}:{seconds:02d}] ({conf:.2f})---")

            break

cap.release()
cv2.destroyAllWindows()
print("---Finished---")



