import pickle
import argparse
import subprocess
import numpy as np 

def main(args): 
    model_name = args.model
    pickled_model = pickle.load(open(f'./Models/{model_name}', 'rb'))

    normal_vector = pickled_model.coef_
    normalised_normal_vector = normal_vector / np.linalg.norm(normal_vector)
    
    latent_code = np.load(f'./dataset_transformed/{args.latent_code}')
    distance = 0
    for k in range(9216): 
        distance += latent_code[0,k]*normalised_normal_vector[0,k]

    latent_code_transformed = latent_code + 2*distance*normalised_normal_vector

    unflatten_latent_code = np.zeros((18,512))

    for j in range (9216): 
        ligne = j//512
        colonne = j%512 
        if colonne == 0 : 
            unflatten_latent_code[ligne-1,511] = latent_code_transformed[0,j] 
        else : 
            unflatten_latent_code[ligne,colonne-1] = latent_code_transformed[0,j]

    attribute_name = model_name.replace('model_','')
    folder_name = args.folder_name

    np.save(f'{folder_name}/{attribute_name}.npy', unflatten_latent_code)

    command = [
        'python', 'generate_image.py', 
        '--outdir', folder_name, 
        '--save_name', attribute_name,
        '--latent_vector', f'{folder_name}/{attribute_name}.npy', 
        '--seeds', '1'
    ]

    subprocess.run(command)

    command = [
        'rm', f'{folder_name}/{attribute_name}.npy'
    ]

    subprocess.run(command)

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()

    parser.add_argument('--model', 
                        type=str,
                        help='Model to load')
    
    parser.add_argument('--latent_code', 
                        type=str,
                        help='Latent code from the image to change')
    
    parser.add_argument('--folder_name', 
                        type=str,
                        help='Folder into which to save the image')

    args = parser.parse_args()
    main(args) 