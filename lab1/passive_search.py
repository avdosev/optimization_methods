import numpy as np

def passive_search(a: float, b: float, N: int, func) -> float:
    step = (b-a)/N
    x_points = np.arange(a, b+step, step)

    value_points = np.array([func(x) for x in x_points])

    min_index = value_points.argmin()
    
    return x_points[min_index]