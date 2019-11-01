machineAcc = 0.000000001

# Метод сопряженных градиентов (Флетчера-Ривса)
# Градиентный поиск минимума
import sys
import numpy as np
from scipy import optimize

FRPath = []

def FR(x0, h, e, f):
    xcur = np.array(x0)
    FRPath.append(xcur)
    h = np.array(h)
    n = len(x0)
    k = 0 # step1
    grad = optimize.approx_fprime(xcur, f, e*e) # step2
    prevgrad = 1
    pk = -1*grad
    while (np.linalg.norm(grad)**2 + machineAcc > e): # step3
        if (k==0 or (k+1)%n==0): # step4
            prevpk = pk
            pk = -1*grad
            bk = 1
        else: 
            bk = (np.linalg.norm(grad)**2)/(np.linalg.norm(prevgrad)**2) # step5
        prevpk = pk
        pk = -1*grad + bk*prevpk # step6
        a = (optimize.minimize_scalar(lambda x: f(xcur+pk*x), bounds=(0,)).x)
        xcur = xcur + a*pk #step8
        FRPath.append(xcur)
        k=k+1 #step8
        prevgrad=grad
        grad=optimize.approx_fprime(xcur, f, e*e) #step2
    return xcur #step10