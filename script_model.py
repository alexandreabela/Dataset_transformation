import os
import subprocess

list_file = os.listdir('/home/alexandreabela/Desktop/stylegan3-projector/Labels/')

for file in list_file: 
    attribute = file.replace('.npy', '')
    command = [
        'python', 'model_selection.py', 
        '--attribute', attribute
    ]
    subprocess.run(command)
    print (f'Model for {attribute} saved')