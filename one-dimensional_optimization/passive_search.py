import numpy as np
from typing import Callable
def passive_search(a: float, b: float, N: int, func: Callable[[float], float]) -> float:
    step = (b-a)/N
    x_points = np.arange(a+step, b, step)

    value_points = np.array([func(x) for x in x_points])

    min_index = value_points.argmin()
    
    return x_points[min_index]