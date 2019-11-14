import scipy.optimize
import numpy as np
from FletcherReeves import FR

def getAuxilitaryFunctionResult(f, r, rest_not_eq, x):
    x1 = x[0]
    x2 = x[1]
    H = 0 
    for i in rest_not_eq:
        H += 1/(0.000001+pow(max(0, i(x1,x2)),2))

    return f(x) + r*H

def distance(a,b):
    sum = 0
    for i in range(len(a)):
        sum += (b[i]-a[i])**2
    return sum


def barrier(x0, f, r, z, eps, rest_not_eq):
    xcur = np.array(x0)
    xnew = None
    atLeastOnePointFound = False
    while (True):
        xtemp = FR(xcur, [1,1], eps, lambda x:getAuxilitaryFunctionResult(f, r, rest_not_eq, x))
        isInside = True
        for neq in rest_not_eq:
            if neq(xtemp[0],xtemp[1]) > eps:
                isInside = False
                break
        if (isInside):
            if (not atLeastOnePointFound):
                atLeastOnePointFound = True
            else:
                xcur = xnew
            xnew = xtemp
        r *= z
        if atLeastOnePointFound and (distance(xcur, xnew)<eps) :
            break
    return xnew
