#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: ancilliary_funcs.py
Author: Luis Alfredo Porras Paez
Email: lporras16[at]gmail[dot]com
Github: https://github.com/lporras
Description:
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

def desafio_2(data_frame):
    for label, serie in data_frame.iteritems():
        print("********************************")
        print(label)
        if serie.dtype == 'object':
            print(serie.value_counts())
        elif serie.dtype == 'float64':
            print(serie.describe())

def desafio_3(dataframe, var, print_list=False):
    if print_list :
        return dataframe[dataframe[var].isna()]
    else:
        null_count = dataframe[var].isnull().sum()
        dataframe_len = len(dataframe)
        return (null_count, null_count/dataframe_len)

def desafio_4(dataframe, var, sample_mean=False, true_mean=False):
    var_drop = dataframe[var].dropna()
    plt.hist(var_drop, color='lightgrey')
    plt.xlabel(var)
    plt.ylabel('Frecuencia')
    if sample_mean:
        sample_var_mean = var_drop.mean()
        plt.axvline(sample_var_mean, lw=3, color='tomato', linestyle='--', label=f"S. Mean ({round(sample_var_mean, 4)}%)")
    if true_mean:
        true_var_mean = df[var].dropna().mean()
        plt.axvline(true_var_mean, lw=3, color='blue', linestyle='--', label=f"T. Mean ({round(true_var_mean, 4)}%)")
    if sample_mean or true_mean:
        plt.legend()
    plt.show()

def desafio_5(dataframe, plot_var, plot_by, global_stat=False, statistic=['mean']):
    grouped_serie = dataframe.groupby(plot_by)[plot_var]
    for stat in statistic:
        if stat == 'mean':
            var_mean = dataframe[plot_var].dropna().mean()
            grouped_means = grouped_serie.mean()
            plt.plot(grouped_means.values, grouped_means.index, 'o')
            plt.axvline(var_mean, color='lightblue', linestyle='--', label=f"Mean ({round(var_mean, 2)}%)")
        elif stat == 'median':
            var_median = dataframe[plot_var].dropna().median()
            grouped_medians = grouped_serie.median()
            plt.plot(grouped_medians.values, grouped_medians.index, 'o')
            plt.axvline(var_median, color='lightgreen', linestyle='--', label=f"Median ({round(var_median, 2)}%)")
        elif stat == 'z_score':
            S=(grouped_serie.mean())
            grouped_z_scores = pd.Series(ss.zscore(S, ddof=1), S.index)
            plt.plot(grouped_z_scores.values, grouped_z_scores.index, 'o')
    if global_stat:
        global_var_serie = df[plot_var].dropna()
        global_var_mean = global_var_serie.mean()
        plt.axvline(global_var_mean, color='blue', linestyle='--', label=f"Global Mean ({round(global_var_mean, 2)}%)")
        if 'median' in statistic:
            global_var_median = global_var_serie.median()
            plt.axvline(global_var_median, color='green', linestyle='--', label=f"Global Median ({round(global_var_median, 2)}%)")
    plt.legend()
    plt.show()


