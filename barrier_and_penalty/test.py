import barrier
import penalty

def f(x):
    x1,x2 = x
    return x1**2+x2**2

def f1(x):
    x1,x2 = x
    return 4*x1**2+8*x1-x2-3

def f2(x):
    x1,x2 = x
    return 4/x1+9/x2+x1+x2

restrictionsOfEquality = [
    [lambda x1,x2: x1+x2+2],
    [lambda x1,x2: x1+x2-2],
    [lambda x1,x2: x1-1],
    []
]

restrictionsOfNotEquality = [
    [lambda x1,x2: x1+x2-6,lambda x1,x2: -x1,lambda x1,x2: -x2],
    [lambda x1,x2: x1+x2-4,lambda x1,x2: -x1,lambda x1,x2: -x2],
    [lambda x1,x2: x1+x2-2],
    [lambda x1,x2: -x1+1,lambda x1,x2: x1+x2-2],
    []
]

while(True):
    print("""Выберете функцию которую нужно минимизировать:
    1 - 1.1
    2 - 1.2
    3 - 1.3
    4 - 2.5
    5 - 2.6
    """)
    chosenFoon = int(input())

    if chosenFoon == 1:
        print("\nМинимизируемая функция: x1^2+x2^2")
        print("Метод штрафных функций: ")
        res = penalty.penalty([0.,0.], 
        f, 
        0.1, 
        10, 
        0.01,
        restrictionsOfEquality[1], 
        []) 
        r = ""
        for j in res:
            r+=f"{j:.{5}f} "
        print(r) 
        print (res[0]**2+res[1]**2)

    elif chosenFoon == 2:
        print("\nМинимизируемая функция: x1^2+x2^2")
        print("Метод штрафных функций: ")
        res = penalty.penalty([0.,1.], 
        f, 
        0.1, 
        10, 
        0.01,
        restrictionsOfEquality[2], 
        restrictionsOfNotEquality[2]) 
        r = ""
        for j in res:
            r+=f"{j:.{5}f} "
        print(r) 
        print (res[0]**2+res[1]**2)

    elif chosenFoon == 3:
        print("\nМинимизируемая функция: x1^2+x2^2")
        print("Метод барьерных функций: ")
        res = penalty.penalty([2.,2.], 
        f, 
        0.1, 
        10, 
        0.01,
        [], 
        restrictionsOfNotEquality[3]) 
        r = ""
        for j in res:
            r+=f"{j:.{5}f} "
        print(r) 
        print (res[0]**2+res[1]**2)

    elif chosenFoon == 4:
        print("\nМинимизируемая функция: 4*x1^2+8*x1-x2-3")
        print("Метод барьерных функций: ")
        res = barrier.barrier([-1.,-7.], 
        f1, 
        100, 
        0.5, 
        0.005,
        restrictionsOfEquality[0])
        r =""
        for j in res:
            r+=f"{j:.{5}f} "
        print(r)
        print (4*res[0]**2+8*res[0]-res[1]-3)

    elif chosenFoon == 5:
        print("\nМинимизируемая функция: 4/x1+9/x2+x1+x2")
        print("Метод штрафных функций при ограничении (а): ")
        res = penalty.penalty([4.,5.], 
        f2, 
        0.1, 
        10, 
        0.01,
        [], 
        restrictionsOfNotEquality[0]) 
        r = ""
        for j in res:
            r+=f"{j:.{5}f} "
        print(r)
        print (4/res[0]+9/res[1]+res[0]+res[1])

        print("Метод штрафных функций при ограничении (б): ")
        res = penalty.penalty([2.,3.], 
        f2, 
        0.1, 
        10, 
        0.1,
        [], 
        restrictionsOfNotEquality[1]) 
        r = ""
        for j in res:
            r+=f"{j:.{5}f} "
        print(r)
        print (4/res[0]+9/res[1]+res[0]+res[1])


    

