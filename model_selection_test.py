import argparse
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV

MLP = MLPClassifier()

def main(args): 
    attribute = args.attribute

    targets = np.asarray(np.load(f'./targets_subdataset/targets_{attribute}.npy'))
    features = np.asarray(np.load('./data_training/subdata_training_.npy'))

    nsamples, nx, ny = features.shape
    features_final = features.reshape((nsamples,nx*ny))

    mlp_param_grid = {
    'activation' : ['relu'],
    'solver' : ['sgd'],
    'max_iter': [5000],
    'hidden_layer_sizes' : [5000]
    }
    MLP_grid = GridSearchCV(
    estimator = MLP, 
    param_grid = mlp_param_grid, 
    cv = 3, 
    verbose = 2,
    scoring = 'roc_auc'
    )
    MLP_grid.fit(features_final,targets)

    print('MLP classifier best roc_auc score :', MLP_grid.best_score_)
    print('-------------------------------------------------------------')
    print('MLP classifier best estimator :', MLP_grid.best_estimator_)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--attribute', 
                        type=str,
                        help='Attribute you want to select the model for')

    args = parser.parse_args()
    main(args)