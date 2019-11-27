import numpy as np
import random
from typing import Callable

def simulated_annealing(func: Callable[[np.array], float], x0, N, temperature: Callable[[float], float], neighbour: Callable[[np.array, float], np.array], passage: Callable[[float, float, float], float]):
    k = 1
    x = np.array(x0)
    x_optimal = x
    e_optimal = func(x_optimal)
    while k < N:
        t = temperature(k)
        x_new = neighbour(x, t)
        e_old = func(x)
        e_new = func(x_new)
        if e_new < e_old or passage(e_old, e_new, t) >= random.random():
            x = x_new
        
        if e_new < e_optimal:
            x_optimal = x_new
            e_optimal = e_new

        k += 1

    if func(x) < e_optimal:
        x_optimal = x

    return x_optimal