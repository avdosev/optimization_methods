machineAcc = 0.000000001

# Бинарный поиск
def bin(a,b,e,d,f):
    while ((b-a)/2 >= e):
        x1 = (a+b)/2 - d
        x2 = (a+b)/2 + d
        if (f(x1)<=f(x2)):
            b = x2
        else:
            a = x1
    return (a+b)/2

# Метод Дэвиса-Свенна-Кэмпи
# Находит отрезок с минимумом
def DSK(x0, h, f):
    xcur = x0
    xnext = x0+h
    cur = f(xcur)
    next = f(xnext)
    if (cur>next):
        a = x0
        k = 2
    else:
        xcur = x0
        xnext = x0-h
        next = f(xnext)
        if (next>=cur):
            return [x0-h, x0+h]
        else:
            b = x0
            h = -h
            k = 2
    while (True):
        xcur = xnext
        xnext = x0 + h*pow(2,(k-1))
        cur = next
        next = f(xnext)
        if (cur<next):
            if (h>0):
                b = xnext
            else:
                a = xnext
            return [a,b]
        else:
            if (h>0):
                a = xcur
            else:
                b = xcur
            k=k+1

# Метод сопряженных градиентов (Флетчера-Ривса)
# Градиентный поиск минимума
import sys
import numpy as np
from scipy import optimize
def FR(x0, h, e, f):
    xcur = np.array(x0)
    h = np.array(h)
    n = len(x0)
    k = 0 # step1
    grad = optimize.approx_fprime(xcur, f, e*e) # step2
    prevgrad = 1
    pk = -1*grad
    while (np.linalg.norm(grad) + machineAcc > e): # step3
        if (k==0 or (k+1)%n==0): # step4
            prevpk = pk
            pk = -1*grad
            bk = 1
        else: 
            bk = (np.linalg.norm(grad)**2)/(np.linalg.norm(prevgrad)**2) # step5
        prevpk = pk
        pk = -1*grad + bk*prevpk # step6
        res = DSK(0, h[k%n], lambda x: f(xcur+pk*x)) #step7
        a = bin(res[0], res[1], e, e/10, lambda x: f(xcur+pk*x))
        xcur = xcur + a*pk #step8
        k=k+1 #step8
        prevgrad=grad
        grad=optimize.approx_fprime(xcur, f, e*e) #step2
    return xcur #step10

def f1(x):
    return 4*pow((x[0]-5),2) + pow((x[1]-6),2) #ожидаемый — [5;6]

def f2(x):
    return pow(x[0]*x[0]+x[1]-11, 2) + pow(x[0]+x[1]*x[1]-7,2)

def f3(x):
    return (100*(x[1]-x[0]**2)**2 + 
    (1-x[0])**2 + 
    90*(x[3]-x[2]**2)**2 + 
    (1-x[2])**2 + 
    10.1*((x[1]-1)**2+(x[3]-1)**2) + 
    19.8*(x[1]-1)*(x[3]-1))

funcToTest = f1
startPoint = [0.,0.]
step = [1.,1.]
precision = 0.01
res = FR(startPoint,step,precision, funcToTest)
print(res)
print(funcToTest(res))