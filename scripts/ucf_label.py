import os

txt_path = "ucf_label/testlist03.txt"
output_path = txt_path 

modified_label = []

with open(txt_path,'r') as train_file:
    for line in train_file:
        label = line.strip().split()

        if len(label) == 2:
            video_path = label[0]
            label_number = int(label[1])
            
            new_label = 3
            
            if label_number ==74:
                new_label = 2
            
            modified_label.append(f"{video_path} {new_label}")

    with open(output_path, 'w') as outfile:
        outfile.write('\n'.join(modified_label))
