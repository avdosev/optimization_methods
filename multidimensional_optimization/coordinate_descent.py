import numpy as np

def coordinate_descent(N: int, eps: float = 0.0001):
    k = 0
    h = np.array([0]*N)
    x = np.array([0]*N)
    step_crushing_ratio = 0.1
    def euclidean_norm(h: np.array):
        return np.sqrt(np.sqr(h).sum())
    while euclidean_norm < eps:
        for i in range(1, N+1):
            ak = 1 # argmin(...)
            x[k+1][i] = x[k][i] + ak*h

        if x[k+1] != x[k]:
            k+=1
            continue 
        h *= step_crushing_ratio
    return x[k+1]