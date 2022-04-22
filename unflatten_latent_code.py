import os
import argparse
import numpy as np

def main(args):  
    latent_code = np.asarray(np.load(args.latent_code))[0]
    unflatten_final = np.zeros((18,512))

    for j in range (9216): 
        ligne = j//512
        colonne = j%512 
        if colonne == 0 : 
            unflatten_final[ligne-1,511] = latent_code[0,j] 
        else : 
            unflatten_final[ligne,colonne-1] = latent_code[0,j] 
    
    print(f'Transform {latent_code.shape} to {unflatten_final.shape}')
    latent_file = latent_file.replace('.npy','')
    np.save(f'./{latent_file}_unflatten.npy', unflatten_final)

if __name__ == '__main__' : 
    parser = argparse.ArgumentParser()

    parser.add_argument('--latent_code', 
                        type=str,
                        help='latent code to unflat')

    args = parser.parse_args()
    main(args)

