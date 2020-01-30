#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: lec1_graphs.py
Author: Ignacio Soto Zamorano
Email: ignacio[dot]soto[dot]z[at]gmail[dot]com
Github: https://github.com/ignaciosotoz
Description: Assorted functions for regularization strategies lecture - ADL
"""


import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import Ridge, Lasso, ElasticNet, LinearRegression
from sklearn.pipeline import Pipeline




def quadratic_data(gen_plot=False):
    """TODO: Docstring for quad_plor.
    :returns: TODO

    """
    np.random.seed(1128)
    m = 100
    X= 3 * np.random.rand(m, 1)
    y = 1 - 0.4 * X +np.random.randn(m, 1) / 1.5
    X_new = np.linspace(0, 3, 100).reshape(100, 1)

    if gen_plot is True:
        plt.scatter(X, y, color='slategrey', marker='d', alpha=.4)
        plt.xlabel('X')
        plt.ylabel('y')
    else:
        return X, y

def plot_regularization(model_spec, poly_degree, lambdas, **kwargs):
    """TODO: Docstring for plot_regularization.

    :model: TODO
    :poly_degree: TODO
    :lambdas: TODO
    :**kwargs: TODO
    :returns: TODO

    """

    # Define variables
    np.random.seed(1128)
    m = 100
    X= 3 * np.random.rand(m, 1)
    y = 1 - 0.4 * X +np.random.randn(m, 1) / 1.5
    X_new = np.linspace(0, 3, 100).reshape(100, 1)

    for lmbd, clr in zip(lambdas,[['#4477AA', ':'], ['#66CCEE', '--'], ['#228833', '-']]):
        if len(lambdas) > 0:
            tmpmodel = model_spec(lmbd, **kwargs)
        else:
            tmpmodel = LinearRegression()
        if poly_degree is True:
            tmpmodel = Pipeline([
                ('polynomial_feats', PolynomialFeatures(degree=10, include_bias=False)),
                ('scaler', StandardScaler()),
                ('regularization', tmpmodel),
            ])

        tmpmodel.fit(X, y)
        y_hat_regularized = tmpmodel.predict(X_new)

        plt.plot(X_new, y_hat_regularized, color=clr[0], linestyle=clr[1], linewidth=2, label=r'$\lambda$' + '= {}'.format(lmbd))
        plt.scatter(X, y, color='slategrey', marker='d', alpha=.4)
        # Define axis limits
        plt.axis([0, 3, -1, 3])

        plt.legend()



def bgd_path(theta, X, y, l1, l2, core = 1, eta = 0.1, n_iterations = 50):
    path = [theta]
    for iteration in range(n_iterations):
        gradients = core * 2/len(X) * X.T.dot(X.dot(theta) - y) + l1 * np.sign(theta) + 2 * l2 * theta

        theta = theta - eta * gradients
        path.append(theta)
    return np.array(path)

def ridge_lasso_grid():
    """TODO: Docstring for ridge_lasso_grid.
    :returns: TODO

    """

    t1a, t1b, t2a, t2b = -1, 3, -1.5, 1.5
    # ignoring bias term
    t1s = np.linspace(t1a, t1b, 500)
    t2s = np.linspace(t2a, t2b, 500)
    t1, t2 = np.meshgrid(t1s, t2s)
    T = np.c_[t1.ravel(), t2.ravel()]
    Xr = np.array([[-1, 1], [-0.3, -1], [1, 0.1]])
    yr = 2 * Xr[:, :1] + 0.5 * Xr[:, 1:]

    J = (1/len(Xr) * np.sum((T.dot(Xr.T) - yr.T)**2, axis=1)).reshape(t1.shape)

    N1 = np.linalg.norm(T, ord=1, axis=1).reshape(t1.shape)
    N2 = np.linalg.norm(T, ord=2, axis=1).reshape(t1.shape)

    t_min_idx = np.unravel_index(np.argmin(J), J.shape)
    t1_min, t2_min = t1[t_min_idx], t2[t_min_idx]

    t_init = np.array([[0.25], [-1]])


    for i, N, l1, l2, title in ((0, N1, 0.5, 0, "Lasso"), (1, N2, 0,  0.1, "Ridge")):
        JR = J + l1 * N1 + l2 * N2**2

        tr_min_idx = np.unravel_index(np.argmin(JR), JR.shape)
        t1r_min, t2r_min = t1[tr_min_idx], t2[tr_min_idx]

        levelsJ=(np.exp(np.linspace(0, 1, 20)) - 1) * (np.max(J) - np.min(J)) + np.min(J)
        levelsJR=(np.exp(np.linspace(0, 1, 20)) - 1) * (np.max(JR) - np.min(JR)) + np.min(JR)
        levelsN=np.linspace(0, np.max(N), 10)

        path_J = bgd_path(t_init, Xr, yr, l1=0, l2=0)
        path_JR = bgd_path(t_init, Xr, yr, l1, l2)
        path_N = bgd_path(t_init, Xr, yr, np.sign(l1)/3, np.sign(l2), core=0)

        plt.subplot(221 + i * 2)
        plt.contour(t1, t2, N, levels=levelsN)
        plt.plot(path_J[:, 0], path_J[:, 1],marker='o', color='grey')
        plt.plot(path_N[:, 0], path_N[:, 1],marker='^', color='lightgrey')
        plt.plot(t1_min, t2_min, "rs")
        plt.title(r"Norma $\ell_{}$".format(i + 1))
        plt.axis([t1a, t1b, t2a, t2b])
        if i == 1:
            plt.xlabel(r"$\theta_1$")
        plt.ylabel(r"$\theta_2$")

        plt.subplot(222 + i * 2)
        plt.contour(t1, t2, JR, levels=levelsJR, alpha=0.9)
        plt.plot(path_JR[:, 0], path_JR[:, 1], marker='o', color='grey')
        plt.plot(t1r_min, t2r_min, color='slategrey')
        plt.title(title)
        plt.axis([t1a, t1b, t2a, t2b])
        if i == 1:
            plt.xlabel(r"$\theta_1$")
        plt.tight_layout()
