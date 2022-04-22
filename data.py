import os 
import numpy as np

n_subdataset = len(os.listdir('/home/alexandreabela/Desktop/stylegan3-projector/dataset_training_transformed/'))

data = []

for i in range(1000):
    int = 35000 + i
    if os.path.exists(f'/home/alexandreabela/Desktop/stylegan3-projector/dataset_training_transformed/{int}.npy'): 
        data_to_add = np.load(f'/home/alexandreabela/Desktop/stylegan3-projector/dataset_training_transformed/{int}.npy').tolist()
        data.append(data_to_add)
    print(f'{i}/{n_subdataset}')

data = np.asarray(data)
np.save(f'/home/alexandreabela/Desktop/stylegan3-projector/data_training/data_training_.npy', data)