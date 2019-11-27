import numpy as np
import random

def simulated_annealing(func: Callable[[np.array], float], x0, N, temperature: Callable[[float], float], neighbour: Callable[[float], float], passage: Callable[[float, float, float], float]):
    k = 1
    random.seed(42)
    dim = len(x0)
    x = np.array(x0)
    while k < N:
        t = temperature(k / N)
        x_new = neighbour(x)
        e_old = func(x)
        e_new = func(x_new)
        if passage(e_old, e_new, t) >= random.random(0, 1):
            x = x_new
        k += 1
    return x