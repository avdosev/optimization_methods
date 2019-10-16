import numpy as np
from typing import Callable

def coordinate_descent(func: Callable[..., float], N: int, odm: Callable[[Callable[[float], float], float, float], float], eps: float = 0.0001, step_crushing_ratio: float = 0.1):
    k = 0
    h = np.array([1.0]*N)
    x_points = [ [0]*N ]

    def euclidean_norm(h: np.array):
        return np.sqrt((h**2).sum())
    
    while euclidean_norm(h) > eps:
        x_points.append([0]*N)
        for i in range(N):
            args = x_points[k].copy()
            
            def odm_func(x):
                nonlocal i, func, args
                args[i] = x
                return func(*args)
                
            ak = odm(odm_func, args[i], h[i])  

            x_points[k+1][i] = ak

        if any([abs(x_points[k+1][i] - x_points[k][i]) > eps for i in range(N)]):
            k+=1
            continue 

        h *= step_crushing_ratio
    
    return x_points[k+1]