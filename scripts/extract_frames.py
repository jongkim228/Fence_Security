import cv2
import os

video_path = "/workspaces/Fence_Security/videos"
frames_dir = "/workspaces/Fence_Security/frames"

def extract(video_path,frames_dir):
    for file_name in os.listdir(video_path):
        if file_name.endswith(".mp4"):
            video_file = os.path.join(video_path,file_name)
            cap = cv2.VideoCapture(video_file)

            if not cap.isOpened():
                print(f"open failed")
                continue

            video_name = os.path.splitext(file_name)[0]
            output_dir = os.path.join(frames_dir,video_name)
            os.makedirs(output_dir, exist_ok=True)

            count = 0

            frame_index = 0
            success, frame = cap.read()
            while success:
                if frame_index % 5 == 0:
                    frame_path = os.path.join(output_dir,f"frame{count:004d}.jpg")
                    cv2.imwrite(frame_path,frame)
                    count += 1
                frame_index += 1
                success, frame = cap.read()


            cap.release()

extract(video_path, frames_dir)


    




    