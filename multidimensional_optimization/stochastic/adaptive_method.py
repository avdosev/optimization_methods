import numpy as np
from typing import Callable, List


def adaptive_method(func: Callable[[np.array], float], x0, M: int, N: int, eps: float = 0.0001):
    x = x0
    t = 1
    k = 0
    a = 1
    b = 0.5
    j = 1
    while k < N:
        e = np.random.uniform(-1, 1, len(x))
        y = x + t * e / np.linalg.norm(e)

        if func(y) < func(x):
            z = x + a * (y - x)
            if func(z) < func(x):
                x = z
                t *= a
                k += 1
                j = 1
                continue

        if j < M:
            j += 1
        else:
            if t <= eps:
                break

            t *= b
            j = 1

    return x
