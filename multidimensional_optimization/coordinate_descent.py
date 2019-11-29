import numpy as np
from typing import Callable, List

def coordinate_descent(func: Callable[..., float], x0: List[float], odm: Callable[[Callable[[float], float], float, float], float], eps: float = 0.0001, step_crushing_ratio: float = 0.99):
    k = 0
    N = len(x0)
    h = np.array([1.0]*N)
    x_points = [ x0 ]
    
    while h[0] > eps:
        x_points.append([0]*N)
        for i in range(N):
            args = x_points[k].copy()
            
            def odm_func(x):
                nonlocal i, func, args
                args[i] = x
                return func(*args)
                
            ak = odm(odm_func, args[i], h[i])  

            x_points[k+1][i] = ak

        if np.linalg.norm(np.array(x_points[k+1])-np.array(x_points[k])) <= eps:
            break

        k += 1
        h *= step_crushing_ratio
    
    return x_points[len(x_points)-1]