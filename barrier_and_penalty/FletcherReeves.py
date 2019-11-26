machineAcc = 0.000000001

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
    grad = optimize.approx_fprime(xcur, f, e**4) # step2
    prevgrad = 1
    pk = -1*grad
    while (any([abs(grad[i]) > e**2 for i in range(n)])): # step3
        if (k%n==0): # step4
            pk = -1*grad
        else: 
            bk = (np.linalg.norm(grad)**2)/(np.linalg.norm(prevgrad)**2) # step5
            prevpk = pk
            pk = -1*grad + bk*prevpk # step6
        a = (optimize.minimize_scalar(lambda x: f(xcur+pk*x), bounds=(0,)).x)
        xcur = xcur + a*pk #step8
        k=k+1 #step8
        prevgrad=grad
        grad=optimize.approx_fprime(xcur, f, e**4) #step2
    return xcur #step10