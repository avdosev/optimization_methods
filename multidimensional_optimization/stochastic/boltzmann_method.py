import random
import math
import numpy as np
from scipy.stats import cauchy
from stochastic.simulated_annealing_algorithm import simulated_annealing

def boltzmann_method(x0, t0, function, N=2500):
    """
    алгоритм имитации отжига
    метод Больцмана
    """
    annealing = lambda k: t0 / math.log(1 + k)
    passage = lambda e_old, e_new, t: 1 / (1 + math.exp((e_new - e_old) / t))
    neighbour = lambda x_old: x_old + np.random.standard_cauchy(len(x_old)) 
    return simulated_annealing(function, x0, N, annealing, neighbour, passage)