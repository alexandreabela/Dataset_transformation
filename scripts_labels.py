import os 
import subprocess


list_dataset = os.listdir('/home/alexandreabela/Desktop/stylegan3-projector/dataset')

for i in range(len(list_dataset)): 
    img_file = list_dataset[i]
    command = [
        'python', 'labels_to_dict.py', 
        '--img_file', f'/home/alexandreabela/Desktop/stylegan3-projector/dataset/{img_file}'
    ]
    subprocess.run(command)