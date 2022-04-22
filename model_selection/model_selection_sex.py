#===============================

# Mettre lien video youtube 

#===============================

import argparse
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, GridSearchCV
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score

def main(args): 
    attribute = args.attribute

    targets = np.load(f'./targets/targets_{attribute}.npy')
    features = np.load('./data_training/data_training.npy')

    RF = RandomForestClassifier()
    MLP = MLPClassifier()
    LR = LogisticRegression()
    SVM = SVC()


    rf_param_grid = {
    'criterion' : ['gini','entropy'],
    'max_features' : ['auto','sqrt','log2'],
    'n_estimators' : [100, 500, 1000, 5000, 10000]
    }
    RF_grid = GridSearchCV(
    estimator = RF, 
    param_grid = rf_param_grid, 
    cv = 5, 
    scoring = 'roc_auc_score'
    )
    RF_grid.fit(features,targets)
    RF_grid.cv_results_

    mlp_param_grid = {
    'activation' : ['identity','logistic','tanh','relu'],
    'solver' : ['lbfgs','sgd','adam'],
    'learning_rate' : ['constant', 'invscaling', 'adaptative'],
    'hidden_layer_sizes' : [100, 500, 1000]
    }
    MLP_grid = GridSearchCV(
    estimator = MLP, 
    param_grid = mlp_param_grid, 
    cv = 5, 
    scoring = 'roc_auc_score'
    )
    MLP_grid.fit(features,targets)


    lr_param_grid = {
    'penalty' : ['l1','l2', 'elasticnet', 'none'],
    'solver' : ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
    'C' : [0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100]
    }
    LR_grid = GridSearchCV(
    estimator = LR, 
    param_grid = lr_param_grid, 
    cv = 5, 
    scoring = 'roc_auc_score'
    )
    LR_grid.fit(features,targets)


    svc_param_grid = {
    'gamma' : ['scale','auto'],
    'kernel' : ['linear', 'poly', 'rbf', 'sigmoid', 'precomputed'],
    'C' : [0.01, 0.05, 0.1, 0.5, 1, 5, 10, 50, 100]
    }
    SVC_grid = GridSearchCV(
    estimator = SVM, 
    param_grid = rf_param_grid, 
    cv = 5, 
    scoring = 'roc_auc_score'
    )
    SVC_grid.fit(features,targets)

    print('-------------------------------------------------------------------')
    #print('RF classifier best roc_auc score :', RF_grid.best_score_)
    print('MLP classifier best roc_auc score :', MLP_grid.best_score_)
    print('LR classifier best roc_auc score :', LR_grid.score_)
    print('SVM classifier best roc_auc score :', SVC_grid.best_score_)
    print('-------------------------------------------------------------------')
    print('RF classifier best estimator :', RF_grid.best_estimator_)
    print('MLP classifier best estimator :', RF_grid.best_estimator_)
    print('LR classifier best estimator :', RF_grid.best_estimator_)
    print('SVM classifier best estimator :', RF_grid.best_estimator_)
    print('-------------------------------------------------------------------')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--attribute', 
                        type=str,
                        help='Attribute you want to select the model for')

    args = parser.parse_args()
    main(args)