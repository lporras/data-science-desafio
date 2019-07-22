#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: lec2_graphs.py
Author: Ignacio Soto Zamorano
Email: ignacio[dot]soto[dot]z[at]gmail[dot]com
Github: https://github.com/ignaciosotoz
Description: Ancilliary file for intro to data science - adl
"""


import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def generate_pet():
    """docstring for generate_pet"""
    return np.random.choice(['Gato', 'Perro'])


def simulate_pets_pr(n_sims):
    """docstring for simulate_pets_pr"""
    dos_perros = 0
    perro_viejo = 0
    at_least_un_perro = 0
    np.random.seed(11238)
    for _ in range(n_sims):
        young_pet = generate_pet()
        old_pet = generate_pet()
        if old_pet == 'Perro':
            perro_viejo += 1
        if old_pet == 'Perro' and young_pet == 'Perro':
            dos_perros += 1
        if old_pet == 'Perro' or young_pet == 'Perro':
            at_least_un_perro += 1

    print("Pr(2 perros | perro viejo): ", dos_perros / perro_viejo)
    print("Pr(2 perros | por lo menos 1 perro): ", dos_perros / at_least_un_perro)

def simulate_bayes(x_axis_n = 100, sample_size = 500, p = .7, prior_pr = .5, prior_size = 1000):
    """docstring for simulate_bayes"""
    xaxis = np.linspace(0, 1, x_axis_n)
    empirical_sample = np.random.binomial(n=1, p=p, size=sample_size)
    likelihood = np.array([np.product(stats.bernoulli.pmf(empirical_sample, i)) for i in x_axis_n])
    likelihood_point = np.mean(likelihood)
    prior_sample = np.random.binomial(n=1, p=prior_pr, size=prior_size)
    prior_prob = np.array([np.product(stats.bernoulli.pmf(prior_sample, i)) for i in x_axis_n])
    prior_prob = prior_prob / np.sum(prior_prob)
    posterior_prob = [likelihood[i] * prior_prob[i] for i in range(prior_prob.shape[0])]
    posterior_prob = posterior_prob / np.sum(posterior_prob)

    plt.subplot(3, 1, 1)
    plt.vlines(xaxis, 0, likelihood, color='tomato')
    plt.title('Verosimilitud (Likelihood)')
    plt.subplot(3, 1, 2)
    plt.vlines(xaxis, 0, prior_prob)
    plt.title("Probabilidad a priori")
    plt.subplot(3, 1, 3)
    plt.vlines(xaxis, 0, posterior_prob)
    plt.title("Probabilidad a posteriori")


def graph_venn():
    """display joint events"""
    venn2(subsets=(14, 13, 5), set_labels=('Batallas\nBaratheon', 'Muertes\nImportantes'))
    plt.title(r'Pr($A\cap B$): Eventos conjuntos. Baratheon y Muertes')

def graph_disjointed():
    """docstring for graph_disjointed"""
    venn2(subsets=(14, 10, 0), set_labels=('Batallas\nBaratheon', 'Batallas\nStark'))
    plt.title(r'Pr($A \cup B$): Eventos independientes. Baratheon Ó Stark')
