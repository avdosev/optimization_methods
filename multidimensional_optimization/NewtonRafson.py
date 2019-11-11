machineAcc = 0.000000001

import sys
import numpy as np
from scipy import optimize

def NR(x0, h, e, f):
    xcur = np.array(x0)
    Path.append(xcur)
    h = np.array(h)
    n = len(x0)

    grad = optimize.approx_fprime(xcur, f, e*e) # step2
    while (np.linalg.norm(grad)**2 + machineAcc > e): # step3
        
        
        prevpk = pk
        pk = -1*grad + bk*prevpk # step6
        a = (optimize.minimize_scalar(lambda x: f(xcur+pk*x), bounds=(0,)).x)
        xcur = xcur + a*pk #step8
        Path.append(xcur)
        k=k+1 #step8
        prevgrad=grad
        grad=optimize.approx_fprime(xcur, f, e*e) #step2
    return xcur #step10