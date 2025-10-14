import cv2
import os

def video_to_frames(video_path, output_folder, seconds_interval=5):
    """
    비디오 파일을 지정된 시간(초) 간격으로 프레임 이미지로 변환하는 함수

    :param video_path: 비디오 파일 경로
    :param output_folder: 프레임을 저장할 폴더 경로
    :param seconds_interval: 프레임을 저장할 시간 간격 (초)
    """
    # 비디오 파일 이름 (확장자 제외)으로 하위 폴더 생성
    video_filename = os.path.splitext(os.path.basename(video_path))[0]
    save_path = os.path.join(output_folder, video_filename)
    
    # 폴더가 없으면 생성
    if not os.path.exists(save_path):
        os.makedirs(save_path)
        print(f"폴더 생성: {save_path}")

    # 비디오 캡처 객체 생성
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"오류: {video_path} 파일을 열 수 없습니다.")
        return

    # 비디오의 FPS(초당 프레임 수) 정보 가져오기
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 저장할 프레임 간격 계산 (예: 30fps 비디오에서 5초 간격 -> 30 * 5 = 150 프레임마다 저장)
    frame_interval = int(fps * seconds_interval)
    
    # 간격이 0이면 오류 방지를 위해 1로 설정
    if frame_interval == 0:
        print("프레임 간격이 0입니다. 기본값 1로 설정합니다.")
        frame_interval = 1
        
    frame_count = 0
    saved_count = 0

    while True:
        # 프레임 읽기
        ret, frame = cap.read()
        
        # 비디오가 끝나면 루프 종료
        if not ret:
            break
        
        # 지정된 간격마다 프레임 저장
        if frame_count % frame_interval == 0:
            # 저장할 파일 이름 설정 (예: frame_0001.jpg)
            frame_filename = f"frame_{saved_count:04d}.jpg"
            cv2.imwrite(os.path.join(save_path, frame_filename), frame)
            saved_count += 1
            
        frame_count += 1

    # 자원 해제
    cap.release()
    print(f"'{video_filename}' 처리 완료. 총 {saved_count}개의 프레임 저장.")


# --- 사용자 설정 ---
# 1. 원본 AVI 비디오들이 있는 폴더 경로
SOURCE_FOLDER = "../ucf_videos"

# 2. 추출된 프레임들을 저장할 상위 폴더 경로
DESTINATION_FOLDER = "../ucf_frames"

# 3. 몇 초마다 프레임을 추출할지 설정
SECONDS_PER_FRAME = 5


# --- 스크립트 실행 ---
if __name__ == "__main__":
    if not os.path.exists(SOURCE_FOLDER):
        print(f"오류: 소스 폴더를 찾을 수 없습니다 - {SOURCE_FOLDER}")
    else:
        # 소스 폴더 내의 모든 파일을 순회
        for filename in os.listdir(SOURCE_FOLDER):
            if filename.lower().endswith('.avi'):
                video_file_path = os.path.join(SOURCE_FOLDER, filename)
                print(f"\n'{filename}' 파일 처리 시작...")
                video_to_frames(video_file_path, DESTINATION_FOLDER, SECONDS_PER_FRAME)