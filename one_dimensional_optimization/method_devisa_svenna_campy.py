from typing import Callable, Tuple

def search_local_min(func: Callable[[float], float], x0: float, h: float = 0.0001) -> Tuple[float, float]:
    f0 = func(x0)
    a = b = x0
    if f0 > func(x0+h):
        a = x0
    elif func(x0-h) >= f0:
        a = x0 - h
        b = x0 + h
        return (a,b)
    else:
        b = x0
        h = -h

    
    def xk(k: int):
        return x0 + (2**(k-1))*h

    
    def assign_if(is_a, value):
        nonlocal a, b
        if is_a:
            a = value
        else:
            b = value

    k = 2
    while True:
        xk0, xk1 = xk(k), xk(k-1)
        if func(xk0) >= func(xk1):
            assign_if(h < 0, xk0)
            break
        else:
            assign_if(h > 0, xk1)
        k += 1

    return (a,b)