# Fence_Security - Climbing Intrusion Detector

A YOLOv5-based climbing intrusion detection system is motivated from military experience, which can improve manual surveiliance system.

## Tech Stack
- Python
- YOLOv5
- PyTorch
- OpenCV
- CVAT (annotation)

## Demo
Test Sample videos are included in the repository(`Test_sample.mov`, `Test_sample1.mov`, `Test_sample2.mov`).
| Walking Detection | Climbing Detection |
|---|---|


|<img width="390" height="395" alt="Demo2" src="https://github.com/user-attachments/assets/fa1ac50b-be25-4f77-9082-45e1674d5aaf" /> | <img width="484" height="502" alt="Demo1" src="https://github.com/user-attachments/assets/62398a38-6521-4dc8-b742-92f9af92910f" />
 |

##Model Performance
Trained on a custom dataset (586 images, annotated with CVAT):
| Class    | Precision | Recall | mAP@0.5 |
|----------|-----------|--------|---------|
| All      | 77.8%     | 79.2%  | 74.3%   |
| Walking  | 63.6%     | 73.4%  | 56.6%   |
| Climbing | 91.9%     | 85.0%  | 91.9%   |

## Dataset
- 586 images across two classes: `walking` and `climbing`
- Fence climbing dataset is acquired from youtube
- Custom footage combined with UCF-101 dataset, in-door climbing motions were relabelled as the `climbing` class to compensate for limited fence climbing data
