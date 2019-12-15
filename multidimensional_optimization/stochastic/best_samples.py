import numpy as np
from typing import Callable, List

def best_samples(func: Callable[[np.array], float], x0, M: int, N: int,  t, R, b):
    x = x0
    k = 0
    while k < N:
        y_xlam = []
        f = []

        for _ in range(M):
            e = np.random.uniform(-1, 1, len(x))
            y = x + t * e / np.linalg.norm(e)
            y_xlam.append(y)
            f.append(func(y))
        
        min_index = np.argmin(f)
        f_min = f[min_index]

        if f_min < func(x):
            x = y_xlam[min_index]
            k += 1
        else:
            if t <= R:
                return x
            elif t > R:
                t *= b
    
    return x