from typing import Callable, Tuple

def search_local_min(func: Callable[[float], float], x0: float, h: float = 0.001) -> Tuple[float, float]:
    f0 = func(x0)
    f_step = func(x0+h)
    if f0 > f_step:
        a = x0
        x_next = x0 + h
    elif func(x0-h) >= f0:
        a = x0 - h
        b = x0 + h
        return (a,b)
    else:
        b = x0
        x_next = x0 - h
        h = -h

    
    def xk(k: int):
        return x0 + (2**(k-1))*h

    k = 2
    while True:
        xk0, xk1 = xk(k), xk(k-1)
        if func(xk0) >= func(xk1):
            if h > 0:
                b = xk0
            else:
                a = xk0
        else:
            if h > 0:
                a = xk1
            else:
                b = xk1

        k += 1

    return (a,b)