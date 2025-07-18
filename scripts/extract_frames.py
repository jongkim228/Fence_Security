import cv2
import os

video_path = "/workspaces/Fence_Security/videos"
frames_dir = "/workspaces/Fence_Security/frames"

def extract(video_path,frames_dir):
    for file_name in os.listdir(video_path):
        if file_name.endwith(".mp4"):
            video_file = os.path.join(video_path,file_name)
            cap = cv2.VideoCapture(video_file)

            video_name = os.path.splitext(file_name)[0]
            output_dir = os.path.join(frames_dir,video_name)
            os.makedirs(output_dir, exist_ok=True)

            count = 0
            success = True
            while success:
                success, frame = cap.read()
                frame_path = os.path.join(output_dir,f"frame{count:004d}")
                cv2.imwrite(frame_path,frame)
                count += 1

            cap.release()

extract(video_path, frames_dir)


    




    