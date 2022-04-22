import os 
import csv
import subprocess

list_file = os.listdir('/home/alexandreabela/Desktop/stylegan3-projector/out/')

list_categorical = ['Sk', 'A', 'Se', 'C', 'P', 'B', 'Hc', 'D', 'Hs']

for file in list_file : 
    file_name = file.replace('.npy', '')
    with open(f'./dictionnary_labels/{file_name}.csv','r') as file: 
        reader = csv.reader(file)
        labels = dict((rows[0],rows[1]) for rows in reader)
    
#Skin tone
    if labels['Sk']==0: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_SK_1'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_SK_2'
        ]
        subprocess.run(command)
    elif labels['Sk']==1:
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_SK_0'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_SK_2'
        ]
        subprocess.run(command)
    else: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_SK_0'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_SK_1'
        ]
        subprocess.run(command)
    
#Age
    if labels['A']==0: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_A_1'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_A_2'
        ]
        subprocess.run(command)
    elif labels['A']==1:
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_A_0'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_A_2'
        ]
        subprocess.run(command)
    else: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_A_0'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_A_1'
        ]
        subprocess.run(command)

#Gender

    command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Se'
        ]
    subprocess.run(command)

#Corpulent
    
    command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_C'
        ]
    subprocess.run(command)

#Particularity

    command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_P'
        ]
    subprocess.run(command)

#Bangs

    command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_B'
        ]
    subprocess.run(command)

#Haircolor
    if labels['Hc']==0: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_1'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_2'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_3'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_4'
        ]
        subprocess.run(command)
    
    elif labels['Hc']==1: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_0'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_2'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_3'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_4'
        ]
        subprocess.run(command)
    
    elif labels['Hc']==2: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_0'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_1'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_3'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_4'
        ]
        subprocess.run(command)

    elif labels['Hc']==3: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_0'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_2'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_1'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_4'
        ]
        subprocess.run(command)
    
    elif labels['Hc']==1: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_0'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_2'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_3'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hc_1'
        ]
        subprocess.run(command)

#Double_chin
    
    command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_D'
        ]
    subprocess.run(command)

#Hair shape
    
    if labels['Hs']==0: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hs_1'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hs_2'
        ]
        subprocess.run(command)
    elif labels['Hs']==1:
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hs_0'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hs_2'
        ]
        subprocess.run(command)
    else: 
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hs_0'
        ]
        subprocess.run(command)
        command = [
            'python', 'change_characteristics.py', 
            '--folder_name', f'./submission/{file_name}/',
            '--latent_code', f'{file_name}.npy',
            '--model', 'model_Hs_1'
        ]
        subprocess.run(command)