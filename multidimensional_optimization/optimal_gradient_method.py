import numpy as np
from scipy import optimize
from typing import Callable, List

def euclidean_norm(h: np.array):
    return np.sqrt((h**2).sum())

def optimal_gradient_method(func: Callable[..., float], N: int, x0: List[float], eps: float = 0.0001, step_crushing_ratio: float = 0.1):
    x = np.array(x0)

    def grad(func, xcur, eps) -> np.array:
        return optimize.approx_fprime(xcur, func, eps**2)

    gr = grad(func, x, eps)
    a = 0

    while euclidean_norm(gr) > eps:
        a = optimize.minimize_scalar(lambda x: func(*[x+a*gr]), bounds=(0,)).x
        x -= a*gr
        gr = grad(func, x, eps)
    
    return x

