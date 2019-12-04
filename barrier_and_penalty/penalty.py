import scipy.optimize
import numpy as np
from optimal_gradient_method import *

def getAuxilitaryFunctionResult(f, r, rest_eq, rest_not_eq, x):
    x1 = x[0]
    x2 = x[1]
    H = 0
    for i in rest_eq:
        H += pow(abs(i(x1,x2)),2)
    for i in rest_not_eq:
        H += pow(max(0, i(x1,x2)),2)
    return f(x) + r*H

def penalty(x0, f, r, z, eps, rest_eq, rest_not_eq):
    xcur = np.array(x0)
    xnew = optimal_gradient_method(lambda x:getAuxilitaryFunctionResult(f, r, rest_eq, rest_not_eq, x), xcur, eps)
    while ((xcur - xnew)**2).sum() > eps:
        r *= z
        xcur = xnew
        xnew = optimal_gradient_method(lambda x:getAuxilitaryFunctionResult(f, r, rest_eq, rest_not_eq, x), xcur, eps)
    return xnew
