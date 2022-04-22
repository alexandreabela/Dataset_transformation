import os 
import subprocess

l = os.listdir("/home/alexandreabela/Downloads/35000")

for i in range(len(l)): 
    file = l[i]
    targetf_name = f'/home/alexandreabela/Downloads/35000/{file}'
    command = [
            'python', 'projector.py',
            '--target', targetf_name
    ]
    subprocess.run(command)

    print(f'Images {str(i)}/{len(l)} treated')

print('Eveything worked correctly')