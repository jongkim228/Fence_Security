import os

ROOT = '../'
FRAMES = os.path.join(ROOT,'frames')
OUTPUT = os.path.join(FRAMES,'train')
VAL_OUTPUT = os.path.join(FRAMES,'val')
SAMPLE5 = os.path.join(FRAMES,'sample5')

for sample_num in range(1,5):
    sample_dir = os.path.join(FRAMES,f'sample{sample_num}')
    i = 0

    filelist = os.listdir(sample_dir)
    filelist.sort()

    for filename in filelist:
        if filename.endswith('.jpg'):
            old_path = os.path.join(sample_dir,filename)
            new_filename = f'sample{sample_num}_frame_{i:04d}.jpg'
            new_path = os.path.join(OUTPUT,new_filename)
            os.rename(old_path,new_path)
            i += 1

sample5_list = os.listdir(SAMPLE5)
sample5_list.sort()

i = 0
for files in sample5_list:
    if files.endswith('.jpg'):
        old_path = os.path.join(SAMPLE5,files)
        new_filename = f'sample5_frame_{i:04d}.jpg'
        new_path = os.path.join(VAL_OUTPUT,new_filename)

        os.rename(old_path,new_path)
        i += 1
        
 
    