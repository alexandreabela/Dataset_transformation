import random
import pickle
import argparse
import numpy as np 

def main(args): 
    model_path = args.model
    pickled_model = pickle.load(open(f'./Models/{model_path}', 'rb'))
    
    coef_hyperplane = pickled_model.coef_
    
    nx, ny = coef_hyperplane.shape
    coef_hyperplane = coef_hyperplane.reshape(nx*ny)

    n_features = len(coef_hyperplane)
    
    points_of_hyperplane = []
    for i in range(9216): 
        point = np.ones(9216)
        for j in range(9215):
            point[j] = random.random()*10 - 5
        for k in range(9215): 
            value = point[k]*coef_hyperplane[k+1] 
        point[9215] = value
        points_of_hyperplane.append(point)

    B = np.ones((n_features,1))

    A = np.array(points_of_hyperplane)

    X = np.linalg.solve(A, B)
    X = np.asarray(X)

    attribute = model_path.replace('/home/alexandreabela/Desktop/stylegan3-projector/Models','')
    attribute = model_path.replace('./Models','')
    attribute = attribute.replace('model_','')
    np.save(f'/home/alexandreabela/Desktop/stylegan3-projector/Vectors/{attribute}.npy', X)


if __name__ == '__main__': 
    parser = argparse.ArgumentParser()

    parser.add_argument('--model', 
                        type=str,
                        help='Model to load')

    args = parser.parse_args()
    main(args) 
