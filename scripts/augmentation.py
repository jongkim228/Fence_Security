import cv2
import albumentations as alb
import os

classes = ["fence", "walking","climbing"]

transform = alb.Compose([
    alb.HorizontalFlip(p=0.5),
    alb.RandomBrightnessContrast(p=0.2)
], bbox_params = A.BboxParams(format='yolo',label_fields=['class']))

frame_train = cv2.imread("../dataset/train")
label_train = "../dataset/train"
frame_val = cv2.imread("../dataset/train")
label_val = "../dataset/val"

for frame in os.listdir(frame_train):
    if frame.endswith(".jpg"):
