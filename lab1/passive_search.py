import numpy as np
import math

def func_1(x):
    return 4*x**3 - 8*x**2 - 11*x + 5



def passive_search(a: float, b: float, N: int, func) -> float:
    step = (b-a)/N
    x_points = np.arange(a, b+step, step)

    value_points = np.array([func(x) for x in x_points])

    min_index = value_points.argmin()
    
    return x_points[min_index]

def main():
    func_number = int(input("Type number of function: "))

    try:
        arr_of_func = [func_1]
        func = arr_of_func[func_number-1]
    except Exception as identifier:
        print("Function not found")
        return
    

    min_index = passive_search(-1, 2, 10, func)
    min_value = func(min_index)

    print(f"x={min_index} y={min_value}")

main()