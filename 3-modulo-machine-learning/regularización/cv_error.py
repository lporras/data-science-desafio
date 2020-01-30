#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: cv_error.py
Author: Ignacio Soto Zamorano
Email: ignacio[dot]soto[dot]z[at]gmail[dot]com
Github: https://github.com/ignaciosotoz
Description: Returns RMSE error metric via CrossValidation.
"""



from sklearn.model_selection import KFold
import sklearn.linear_model as lm
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')



def cv_error(x_train,y_train,k, method = 'OLS', alpha = 1):

    # set training attr matrix and target
    Xm, ym = x_train.as_matrix(), y_train.as_matrix()
    # define kfold manual split
    kf = KFold(n_splits=k)
    # set rmse to 0
    rmse_cv = 0
    # register coefficients
    coef_v = []

    # infer model class given function argument
    if method is 'OLS':
        method_type = lm.LinearRegression(fit_intercept=False)
    elif method is 'ridge':
        method_type = lm.Ridge(alpha=alpha, fit_intercept=False)
    elif method is 'lasso':
        method_type = lm.Lasso(alpha = alpha, fit_intercept=False)
    elif method is 'enet':
        method_type = lm.ElasticNet(alpha=alpha, fit_intercept=False)
    else:
        # raise error if argument isn't valid
        raise TypeError("Method argument is not valid")

    # for each partition
    for train_index, validation_index in kf.split(Xm):
        # instantiate model
        method_type = method_type
        # fit on randomized training
        method_type.fit(Xm[train_index], ym[train_index])
        # append estimates
        coef_v.append(method_type.coef_)
        # create predictions
        yhat_validation = method_type.predict(Xm[validation_index])
        # update rmse metric
        rmse_cv += np.mean(np.power(yhat_validation - ym[validation_index], 2))

    # create a dataframe containing coeficients
    coefs_dataframe = pd.DataFrame(
        # for each inner array, rearrange coeficients
        [[fold[x] for x in range(x_train.shape[1])] for fold in coef_v]
    )

    coefs_dataframe.columns = list(x_train.columns)
    return coefs_dataframe, rmse_cv


def early_stop(X_train, y_train, alphas, tol = 0.1, estimator = 'OLS'):

    cv_alphas, coefs_model, cv_err_model = [], [], []

    if method is 'OLS':
        method_type = lm.LinearRegression(fit_intercept=False)
    elif method is 'ridge':
        method_type = lm.Ridge(fit_intercept=False)
    elif method is 'lasso':
        method_type = lm.Lasso(fit_intercept=False)
    elif method is 'enet':
        method_type = lm.ElasticNet(fit_intercept=False)
    else:
        raise TypeError("Method argument is not valid")

    print(alphas)
    for a in alphas:
        method_type.set_params(alpha = a)
        method_type.fit(X_train, y_train)
        coefs_model.append(method_type.coef_)
        _, cv_err_estimates = cv_error(X_train, y_train, k = 10, method = estimator, alpha = a)
        cv_err_model.append(np.mean(cv_err_estimates))
        cv_alphas.append(a)

        if len(cv_err_model) >= 2 and (cv_err_model[-1] - cv_err_model[-2]) > tol:
            break

    return method_type, cv_err_model, cv_alphas
