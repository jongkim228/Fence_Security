import cv2
import os
import re

video_path = "../videos"
frames_dir = "../frames"

def extract(video_path, frames_dir):
    def extract_number(file_name):
        match = re.search(r'\d+', file_name)
        return int(match.group()) if match else -1

    files = sorted(
        [f for f in os.listdir(video_path) if f.endswith(".avi")],
        key=extract_number
    )

    sample_index = 1

    for file_name in files:
        video_file = os.path.join(video_path, file_name)
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            print(f"open failed: {file_name}")
            continue

        while True:
            output_dir = os.path.join(frames_dir, f"sample{sample_index}")
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                break
            sample_index += 1

        count = 0
        frame_index = 0
        success, frame = cap.read()
        while success:
            if frame_index % 5 == 0:
                frame_path = os.path.join(output_dir, f"sample{sample_index}frame{count:04d}.jpg")
                cv2.imwrite(frame_path, frame)
                count += 1
            frame_index += 1
            success, frame = cap.read()

        cap.release()
        sample_index += 1

extract(video_path, frames_dir)
