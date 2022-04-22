import time
import argparse
import numpy as np
import pickle5 as pickle
from tabnanny import verbose

from sklearn.svm import LinearSVC
from sklearn.model_selection import GridSearchCV

class bcolors: 
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    ROUGE = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def main(args): 
    attribute = args.attribute

    targets = np.asarray(np.load(f'./Labels/{attribute}.npy'))
    features = np.asarray(np.load('./data_training/data_training_.npy'))

    nsamples, nx, ny = features.shape
    features = features.reshape((nsamples,nx*ny))

    SVM = LinearSVC()

    svc_param_grid = {
    'penalty': ['l2'],
    'loss' : ['hinge','squared_hinge'],
    'C': [0.000001, 0.00001, 0.0001, 0.001, 0.01]
    }
    SVC_grid = GridSearchCV(
    estimator = SVM, 
    param_grid = svc_param_grid, 
    cv = 4, 
    verbose = 2,
    scoring = 'roc_auc'
    )
    SVC_grid.fit(features,targets)

    model_name = f'model_{attribute}'

    print(f'{bcolors.GREEN}roc_auc score {SVC_grid.best_score_}')
    print(f'{bcolors.GREEN}best estimator {SVC_grid.best_estimator_}{bcolors.RESET}')
    pickle.dump(SVC_grid.best_estimator_, open(model_name, 'wb'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--attribute', 
                        type=str,
                        help='Attribute you want to select the model for')

    args = parser.parse_args()
    main(args)