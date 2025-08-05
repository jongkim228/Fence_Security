import cv2
import os

video_path = "../videos"
frames_dir = "../frames"

def extract(video_path, frames_dir):
    sample_index = 1
    files = sorted(os.listdir(video_path))
    start_found = False
    for file_name in files:
        if not file_name.endswith(".mp4"):
            continue

        video_file = os.path.join(video_path, file_name)
        cap = cv2.VideoCapture(video_file)
        if not cap.isOpened():
            print(f"open failed: {file_name}")
            continue


        while True:
            output_dir = os.path.join(frames_dir, f"sample{sample_index:01d}")
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
                break
            else:
                sample_index += 1
        video_name = os.path.splitext(file_name)[0]
        output_dir = os.path.join(frames_dir, video_name)
        os.makedirs(output_dir, exist_ok=True)

        count = 0
        frame_index = 0
        success, frame = cap.read()
        while success:
            if frame_index % 5 == 0:
                frame_path = os.path.join(output_dir, f"frame{count:04d}.jpg")
                cv2.imwrite(frame_path, frame)
                count += 1
            frame_index += 1
            success, frame = cap.read()

        cap.release()
    sample_index += 1
extract(video_path, frames_dir)


    




    