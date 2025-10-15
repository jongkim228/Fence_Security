import os
import random
import shutil

# --- 사용자 설정 ---

# 1. 모든 'climbing' 프레임이 하위 폴더 없이 들어있는 원본 폴더 경로
#    (모든 프레임이 한 곳에 모여있는 폴더)
SOURCE_FOLDER = "../ucf_frames_unique"

# 2. 최종적으로 train/val 폴더가 생성될 목적지 폴더
#    (이 안에 images/train, images/val 폴더가 만들어집니다)
DESTINATION_FOLDER = "../dataset1"


def split_single_folder_dataset(source_dir, dest_dir, train_ratio=0.7):
    """
    하위 폴더 없이 이미지 파일만 있는 단일 폴더를 train/val로 분할하는 함수
    """
    print("데이터셋 분할을 시작합니다...")

    # 최종적으로 train, val 이미지가 저장될 경로
    train_path = os.path.join(dest_dir, 'images', 'train')
    val_path = os.path.join(dest_dir, 'images', 'val')

    # 기존에 폴더가 있다면 삭제 후 새로 생성하여 중복 방지
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    os.makedirs(train_path)
    os.makedirs(val_path)
    print(f"'{train_path}' 와 '{val_path}' 폴더를 생성했습니다.")

    # 원본 폴더에서 모든 파일 목록 가져오기
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    
    if not files:
        print(f"오류: '{source_dir}' 폴더에서 이미지 파일을 찾을 수 없습니다.")
        return

    # 파일 목록을 무작위로 섞기
    random.shuffle(files)
    
    # 7:3으로 나눌 기준점 계산
    split_point = int(len(files) * train_ratio)
    
    # 파일 목록 분할
    train_files = files[:split_point]
    val_files = files[split_point:]
    
    # train 폴더로 파일 복사
    print(f"\n--- 학습용(train) 파일 {len(train_files)}개 복사 중 ---")
    for file_name in train_files:
        shutil.copy(os.path.join(source_dir, file_name), os.path.join(train_path, file_name))
            
    # val 폴더로 파일 복사
    print(f"--- 검증용(val) 파일 {len(val_files)}개 복사 중 ---")
    for file_name in val_files:
        shutil.copy(os.path.join(source_dir, file_name), os.path.join(val_path, file_name))
            
    print("\n모든 작업이 완료되었습니다!")
    print(f"총 {len(files)}개 파일 -> 학습용: {len(train_files)}개, 검증용: {len(val_files)}개")


# --- 스크립트 실행 ---
if __name__ == "__main__":
    split_single_folder_dataset(SOURCE_FOLDER, DESTINATION_FOLDER, train_ratio=0.7)