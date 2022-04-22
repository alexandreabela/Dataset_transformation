import os 
import csv
import subprocess

list_file = os.listdir('/home/alexandreabela/Desktop/stylegan3-projector/out/')

for file in list_file : 
    file_name = file.replace('.npy', '')
    
    command = [
        'mkdir', f'./submission/{file_name}'
    ]
    subprocess.run(command)