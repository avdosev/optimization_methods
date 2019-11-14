import scipy.optimize
import numpy as np
from FletcherReeves import FR

def getAuxilitaryFunctionResult(f, r, rest_eq, rest_not_eq, x):
    x1 = x[0]
    x2 = x[1]
    H = 0
    for i in rest_eq:
        H += pow(abs(i(x1,x2)),2)
    for i in rest_not_eq:
        H += pow(max(0, i(x1,x2)),2)
    return f(x) + r*H

def distance(a,b):
    sum = 0
    for i in range(len(a)):
        sum += (b[i]-a[i])**2
    return sum

def penalty(x0, f, r, z, eps, rest_eq, rest_not_eq):
    xcur = np.array(x0)
    xnew = FR(xcur, [1,1], eps, lambda x:getAuxilitaryFunctionResult(f, r, rest_eq, rest_not_eq, x))
    while (distance(xcur, xnew)>eps):
        r *= z
        xcur = xnew
        xnew = FR(xcur, [1,1], eps, lambda x:getAuxilitaryFunctionResult(f, r, rest_eq, rest_not_eq, x))
    return xnew
