import barrier
import penalty
import math

def f(x):
    x1,x2 = x
    return x1**2+x2**2

def f1(x):
    x1,x2 = x
    return math.pow((x1+1.)/3.,3.) + x2

def f2(x):
    x1,x2 = x
    return x1+x2

restrictionsOfEquality = [
    [], # пустышка
    [lambda x1,x2: x1+x2-2],
    [lambda x1,x2: x1-1],
    [],
    [],
    []
]

restrictionsOfNotEquality = [
    [], # пустышка
    [],
    [lambda x1,x2: x1+x2-2],
    [lambda x1,x2: x1+x2-2, lambda x1,x2: -x1+1],
    [lambda x1,x2: -x1+1, lambda x1,x2: -x2],
    # [lambda x1,x2: -x1+1,lambda x1,x2: x1+x2-2]
    [lambda x1,x2: x1*x1-x2, lambda x1,x2: -x1]
]

functionFormul = [
    "x1^2+x2^2",
    "((x1+1)**3)/3 + x2",
    "x1+x2"
]

def out(res, fnc_res):
    r = "".join(f"{j:.{5}f} " for j in res)
    print(r, f"Значение функции в этой точке: {fnc_res}")

def test():
    print("""Выберете функцию которую нужно минимизировать:
    1 - 1.1
    2 - 1.2
    3 - 1.3
    4 - 2.1
    5 - 2.2
    """)
    chosenFoon = int(input("Ваш выбор: "))

    print("\nМинимизируемая функция:", end=" ")
    
    if chosenFoon == 1:
        print(functionFormul[0])
        print("Метод штрафных функций: ")
        res = penalty.penalty([0.,0.], 
            f, 
            0.1, 
            10, 
            0.01,
            restrictionsOfEquality[1], 
            restrictionsOfNotEquality[1]
        ) 
        
        out(res, f(res))

    elif chosenFoon == 2:
        print(functionFormul[0])
        print("Метод штрафных функций: ")
        res = penalty.penalty([0.,1.], 
            f, 
            0.1, 
            10, 
            0.01,
            restrictionsOfEquality[2], 
            restrictionsOfNotEquality[2]
        ) 
        
        out(res, f(res))

    elif chosenFoon == 3:
        print(functionFormul[0])
        print("Метод штрафных функций: ")
        res = penalty.penalty([2.,2.], 
            f, 
            0.1, 
            10, 
            0.01,
            restrictionsOfEquality[3], 
            restrictionsOfNotEquality[3]
        ) 
        
        out(res, f(res))

    elif chosenFoon == 4:
        print(functionFormul[1])
        print("Метод барьерных функций: ")
        res = barrier.barrier([11.,11.], 
            f1, 
            100., 
            0.5, 
            0.005,
            restrictionsOfNotEquality[4])
        
        out(res, f1(res))

    elif chosenFoon == 5:
        print(functionFormul[2])

        print("Метод штрафных функций: ")
        res = penalty.penalty([20.,10.], 
            f2, 
            10., 
            0.5, 
            0.01,
            [], restrictionsOfNotEquality[5])
        out(res, f2(res))

    else:
        print("такой нет")
    
    print()


test()

