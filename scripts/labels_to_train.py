import os

ROOT = '../'
LABELS = os.path.join(ROOT,'labels')
OUTPUT = os.path.join(LABELS,'train')
VAL_OUTPUT = os.path.join(LABELS,'val')
SAMPLE5 = os.path.join(LABELS,'sample5')

for sample_num in range(1,5):
    sample_dir = os.path.join(LABELS,f'sample{sample_num}','obj_train_data')
    i = 0

    files = os.listdir(sample_dir)
    files.sort()

    for filename in files:
        if filename.endswith('.txt'):
            old_path = os.path.join(sample_dir,filename)
            new_filename = f'sample{sample_num}_frame_{i:04d}.txt'
            new_path = os.path.join(OUTPUT,new_filename)
            os.rename(old_path,new_path)
            i += 1

sample5_dir = os.path.join(SAMPLE5, 'obj_train_data')
sample5_list = os.listdir(sample5_dir)
sample5_list.sort()

i = 0
for files in sample5_list:
    if files.endswith('.txt'):
        old_path = os.path.join(sample5_dir,files)
        new_filename = f'sample5_frame_{i:04d}.txt'
        new_path = os.path.join(VAL_OUTPUT,new_filename)

        os.rename(old_path,new_path)
        i += 1
    