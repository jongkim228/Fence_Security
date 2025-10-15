import cv2
import os

def video_to_frames(video_path, output_folder, frame_interval=5):
    """
    비디오 파일을 지정된 프레임 간격으로 이미지로 변환하는 함수
    (프레임 이름에 원본 비디오 이름을 포함하여 중복 방지)

    :param video_path: 비디오 파일 경로
    :param output_folder: 프레임을 저장할 폴더 경로
    :param frame_interval: 이미지를 저장할 프레임 간격
    """
    # 비디오 파일 이름 (확장자 제외)
    video_filename = os.path.splitext(os.path.basename(video_path))[0]
    
    # 이제는 비디오별 하위 폴더를 만들 필요 없이,
    # 모든 프레임을 바로 output_folder에 저장합니다.
    # 만약 폴더가 없다면 생성합니다.
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"폴더 생성: {output_folder}")

    # 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"오류: {video_path} 파일을 열 수 없습니다.")
        return

    # 간격이 0이면 오류 방지를 위해 1로 설정
    if frame_interval <= 0:
        frame_interval = 1
        
    frame_count = 0
    saved_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % frame_interval == 0:
            # --- [핵심 수정] 원본 비디오 파일 이름을 프레임 이름에 포함 ---
            frame_filename = f"{video_filename}_frame_{saved_count:04d}.jpg"
            
            # 저장 경로를 output_folder로 직접 지정
            cv2.imwrite(os.path.join(output_folder, frame_filename), frame)
            saved_count += 1
            
        frame_count += 1

    cap.release()
    print(f"'{video_filename}' 처리 완료. 총 {saved_count}개의 프레임 저장.")


# --- 사용자 설정 ---
SOURCE_FOLDER = "../ucf_videos"
DESTINATION_FOLDER = "../ucf_frames_unique" # 덮어쓰기 방지를 위해 새 폴더 추천
FRAME_SAVE_INTERVAL = 5

# --- 스크립트 실행 ---
if __name__ == "__main__":
    if not os.path.exists(SOURCE_FOLDER):
        print(f"오류: 소스 폴더를 찾을 수 없습니다 - {SOURCE_FOLDER}")
    else:
        for filename in os.listdir(SOURCE_FOLDER):
            if filename.lower().endswith('.avi'):
                video_file_path = os.path.join(SOURCE_FOLDER, filename)
                print(f"\n'{filename}' 파일 처리 시작...")
                # 이제는 비디오별로 폴더를 만들지 않으므로, DESTINATION_FOLDER를 바로 전달
                video_to_frames(video_file_path, DESTINATION_FOLDER, FRAME_SAVE_INTERVAL)