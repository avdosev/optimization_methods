import random
import math
import numpy as np
from scipy.stats import cauchy
from stochastic.simulated_annealing import simulated_annealing


def QA(x0, t0, f, N=2500):
    """
    алгоритм имитации отжига
    метод Коши
    """
    annealing = lambda k: t0 / math.pow(k, 1. / len(x0))
    # passage = lambda e_old, e_new, t: 1. / (1. + math.exp((e_new - e_old) / t))
    passage = lambda e_old, e_new, t: math.exp(-1. * (e_new - e_old) / t)
    neighbour = lambda x_old, t: x_old + t * np.random.standard_cauchy(len(x_old)) 
    return simulated_annealing(function, x0, N, annealing, neighbour, passage)