import HookeJeeves as hj
import FletcherReeves as fr
import optimal_gradient_method as og
import coordinate_descent as cd

def f1(x):
    return 4*pow((x[0]-5),2) + pow((x[1]-6),2) 

def f2(x):
    return pow(x[0]*x[0]+x[1]-11, 2) + pow(x[0]+x[1]*x[1]-7,2)

def f3(x):
    return (100*(x[1]-x[0]**2)**2 + 
    (1-x[0])**2 + 
    90*(x[3]-x[2]**2)**2 + 
    (1-x[2])**2 + 
    10.1*((x[1]-1)**2+(x[3]-1)**2) + 
    19.8*(x[1]-1)*(x[3]-1))

def f4(x):
    x1,x2,x3,x4 = x
    return ((x1+10*x2)**2+
            5*(x3-x4)**2+
            (x2-2*x3)**4+
            10*(x1-x4)**4)

funcsToTestArr = [f1, f2,f3,f4] 
startPointArr = [[0.,0.],[0.,0.],[0.,0.,0.,0.],[1.,1.,1.,1.]]
stepArr = [[1.,1.],[1.,1.],[1.,1.,1.,1.],[1.,1.,1.,1.]]
eps = 0.01
sizeArr = [2,2,4,4]

while (True):
    print("""Выберите метод оптимизации:
    1 - Флетчера-Ривза
    2 - Хука-Дживса
    3 - координатного спуска
    4 - оптимального градиента
    """)
    chosenMethod = int(input())

    print("""
    Выберите функцию для оптимизации:
    1 - ф. Химмельблау №1
    2 - ф. Химмельблау №2
    3 - ф. Вуда
    4 - ф. Пауэлла
    """)
    chosenFun = int(input())
    functionToTest = funcsToTestArr[chosenFun-1]
    step = stepArr[chosenFun-1]

    # print("""
    # Использовать начальную точку по умолчанию? (y/n)
    # """)
    # chosenStartpoint = input()
    
    # if (chosenStartpoint=='y'):
    startPoint = startPointArr[chosenFun-1]
    # else:
    #     print("Введите начальную точку: ")
    #     startPoint = []
    #     for i in range(sizeArr[chosenFun-1]):
    #         startPoint.append(int(input()))

    if chosenMethod==1:
        result = fr.FR(startPoint, step, eps, functionToTest)
    elif chosenMethod==2:
        result = hj.HJ(startPoint, step, eps, functionToTest)
    elif chosenMethod==3:
        def odm(fnc, x0, h):
            res = minimize(fnc, x0, method='nelder-mead',
                options={'xatol': h, 'disp': False})
        result = cd.coordinate_descent(functionToTest, sizeArr[chosenFun-1], odm, eps)
    elif chosenMethod==4:
        result = og.optimal_gradient_method(functionToTest, startPoint, eps)
    
    print("Решение:", result, ", значение функции в этой точке: ", functionToTest(result))