import os 
import numpy as np

n_subdataset = len(os.listdir('/home/alexandreabela/Desktop/stylegan3-projector/subdataset/'))
attribute = 'sex'
list = np.load(f'/home/alexandreabela/Desktop/stylegan3-projector/Labels/{attribute}.npy')

targets = np.zeros(n_subdataset)
j=0

for i in range(1000):
    int = 35000 + i
    if os.path.exists(f'/home/alexandreabela/Desktop/stylegan3-projector/subdataset/{int}.npy'): 
        targets[j]=list[i]
        j+=1

targets = np.asarray(targets)
np.save(f'/home/alexandreabela/Desktop/stylegan3-projector/targets/targets_subdataset_{attribute}.npy', targets)