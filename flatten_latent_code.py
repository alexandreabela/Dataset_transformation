import os
import numpy as np

list_files = os.listdir('/home/alexandreabela/Desktop/stylegan3-projector/out/')
n_subdataset = len(list_files)

for i in range(n_subdataset): 
    latent_file = list_files[i]
    latent_code = np.asarray(np.load(f'/home/alexandreabela/Desktop/stylegan3-projector/out/{latent_file}'))[0]
    flatten_final = np.zeros((1,9216))

    for j in range (9216): 
        ligne = j//512
        colonne = j%512 
        if colonne == 0 : 
            flatten_final[0,j] = latent_code[ligne-1,511] 
        else : 
            flatten_final[0,j] = latent_code[ligne,colonne-1] 
    
    print(f'Transform {latent_code.shape} to {flatten_final.shape}')
    print(f'{i+1}/{n_subdataset}')
    latent_file = latent_file.replace('.npy', '')
    np.save(f'/home/alexandreabela/Desktop/stylegan3-projector/dataset_transformed/{latent_file}', flatten_final)
