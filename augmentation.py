import albumentations as alb
import cv2
import matplotlib.pyplot

transform = alb.Compose(
    [
        alb.HorizontalFLip(p=0.5),
        alb.RandomBrightnessContrast(p=0.2)
    ]
)