import scipy.optimize
import numpy as np
from optimal_gradient_method import *

def getAuxilitaryFunctionResult(f, r, rest_not_eq, x):
    x1, x2 = x
    H = sum(1/(0.000000001+pow(max(0, -i(x1,x2)),2)) for i in rest_not_eq)
    return f(x) + r*H

def barrier(x0, f, r, z, eps, rest_not_eq):
    xcur = np.array(x0)
    xnew = None
    atLeastOnePointFound = False
    while not (atLeastOnePointFound and ( ((xcur-xnew)**2).sum() < eps**2 )):
        xtemp = optimal_gradient_method(lambda x: getAuxilitaryFunctionResult(f, r, rest_not_eq, x), xcur )
        
        isInside = not any(neq(xtemp[0],xtemp[1]) > eps for neq in rest_not_eq)

        if (isInside):
            if not atLeastOnePointFound:
                atLeastOnePointFound = True
            else:
                xcur = xnew
            xnew = xtemp

        r *= z


    return xnew
