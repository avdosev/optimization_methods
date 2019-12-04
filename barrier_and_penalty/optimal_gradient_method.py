import numpy as np
from scipy import optimize
from typing import Callable, List

def euclidean_norm(h: np.array):
    return np.sqrt((h**2).sum())

def optimal_gradient_method(func: Callable[[List[float]], float], x0: List[float], eps: float = 0.001):
    x = np.array(x0)

    def grad(func, xcur, eps) -> np.array:
        return optimize.approx_fprime(xcur, func, eps**2)

    gr = grad(func, x, eps)
    a = 0.

    while any([abs(gr[i]) > eps for i in range(len(gr))]):
    # while euclidean_norm(gr) > eps:
        gr = grad(func, x, eps)
        a = optimize.minimize_scalar(lambda koef: func(*[x+koef*gr])).x
        x += a*gr
        if a == 0:
            break

    return x

