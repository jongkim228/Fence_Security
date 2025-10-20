import os
import shutil

# --- 사용자 설정 ---

# 1. 기준이 될 .txt 라벨 파일들이 있는 폴더
#    (예: v_RockClimbingIndoor_g02_c05_frame_0026_jpg.rf.20bbaff3500b50958c4e688615616009.txt)
REFERENCE_FOLDER = "../ucf_labels1"

# 2. 검색 대상이 될 .jpg 이미지들이 있는 첫 번째 폴더
SOURCE_FOLDER_1 = "../dataset1/images/train"

# 3. 검색 대상이 될 .jpg 이미지들이 있는 두 번째 폴더
SOURCE_FOLDER_2 = "../dataset1/images/val"

# 4. 찾은 .jpg 파일들을 옮겨 놓을 최종 목적지 폴더
#    (폴더가 없으면 자동으로 생성됩니다)
DESTINATION_FOLDER = "./matched_images"


# --- 스크립트 실행 코드 (이 아래는 수정할 필요 없습니다) ---

def find_and_move_partial_match_images(ref_dir, src_dirs, dest_dir):
    """
    기준 폴더의 txt 파일명 일부와 일치하는 jpg 파일들을 검색 대상 폴더들에서 찾아
    목적지 폴더로 이동시킵니다.
    """
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"폴더 생성: {dest_dir}")

    if not os.path.isdir(ref_dir):
        print(f"오류: 기준 폴더를 찾을 수 없습니다 - '{ref_dir}'")
        return

    print(f"'{ref_dir}' 폴더를 기준으로 파일 검색을 시작합니다...")
    moved_count = 0
    
    # 기준 폴더의 모든 .txt 파일을 순회
    for filename_txt in os.listdir(ref_dir):
        if filename_txt.lower().endswith(".txt"):
            
            # --- 핵심 로직: 파일명에서 기준 부분 추출 ---
            # 예: "v_..._frame_0026_jpg.rf.20bba....txt" -> "v_..._frame_0026"
            try:
                base_name = filename_txt.split('_jpg.rf.')[0]
            except IndexError:
                print(f"경고: '{filename_txt}' 파일 이름 형식이 다릅니다. 건너뜁니다.")
                continue
            
            # 찾을 .jpg 파일명
            filename_jpg_to_find = f"{base_name}.jpg"

            # 여러 검색 대상 폴더를 순회
            for src_dir in src_dirs:
                if not os.path.isdir(src_dir):
                    continue

                # 원본 .jpg 파일의 전체 경로
                source_path = os.path.join(src_dir, filename_jpg_to_find)

                # 해당 경로에 파일이 정확히 일치하는지 확인
                if os.path.exists(source_path):
                    destination_path = os.path.join(dest_dir, filename_jpg_to_find)
                    
                    # 파일 이동
                    shutil.move(source_path, destination_path)
                    print(f"이동 완료: '{source_path}' -> '{destination_path}'")
                    moved_count += 1
                    # 한 번 찾으면 다른 폴더에서 더 찾지 않음
                    break 
    
    print(f"\n모든 작업 완료! 총 {moved_count}개의 파일을 '{dest_dir}'(으)로 이동했습니다.")


if __name__ == "__main__":
    source_directories = [SOURCE_FOLDER_1, SOURCE_FOLDER_2]
    find_and_move_partial_match_images(REFERENCE_FOLDER, source_directories, DESTINATION_FOLDER)