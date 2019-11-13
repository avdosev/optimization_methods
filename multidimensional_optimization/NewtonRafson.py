machineAcc = 0.000000001

import sys
import numpy as np
from scipy import optimize


def f1(x):
    x1,x2 = x
    return 4*pow((x1-5),2) + pow((x2-6),2) 

def h1(x):
    x1,x2=x
    return np.array([
        [8, 0],
        [0, 2]        
        ], ndmin=2)

def f2(x):
    x1,x2 = x
    return pow(x1*x1+x2-11, 2) + pow(x1+x2*x2-7,2)

def h2(x):
    x1,x2=x
    return np.array([
        [4*(x1**2+x2-11)+8*x1**2+2,   
        4*x1+4*x2],
        [4*x1+4*x2, 
        4*(x1+x2**2-7)+8*x2**2+2]        
        ], ndmin=2)

def f3(x):
    x1,x2,x3,x4 = x
    return (100*(x2-x1**2)**2 + 
    (1-x1)**2 + 
    90*(x4-x3**2)**2 + 
    (1-x3)**2 + 
    10.1*((x2-1)**2+(x4-1)**2) + 
    19.8*(x2-1)*(x4-1))

def h3(x):
    x1,x2,x3,x4 = x
    return np.array([ 
        [-400*(x2 - x1**2) + 800*x1*2 + 2 , -400*x1 , 0 , 0],
        [-400*x1 , 220.2 , 0 , 19.8],
        [0 , 0 , -360*(x4 - x3**2) + 720*x3**2 + 2 , -360*x3],
        [0 , 19.8 , -360*x3 , 200.2],
        ], ndmin=2)

def f4(x):
    x1,x2,x3,x4 = x
    return ((x1+10*x2)**2+
            5*(x3-x4)**2+
            (x2-2*x3)**4+
            10*(x1-x4)**4)

Path = []

startPointArr = [[0.,0.],[0.,0.],[2.,-1.,-3.,-1.],[3.,-1.,0.,1.]]
stepArr = [[1.,1.],[1.,1.],[1.,1.,1.,1.],[1.,1.,1.,1.]]

def NR(x0, h, e, f, hess_f):
    xcur = np.array(x0)
    Path.append(xcur)
    
    n = len(x0)

    grad = optimize.approx_fprime(xcur, f, e**4) # step2
    while (any([pow(abs(grad[i]),1.5) > e for i in range(n)])): # step3
        h = np.linalg.inv(hess_f(xcur)) # step 4 & 5
        pk = (-1*h).dot(grad) # step 6
        a = (optimize.minimize_scalar(lambda a: f(xcur+pk*a), bounds=(0,)).x) #step7
        xcur = xcur + a*pk #step8
        Path.append(xcur)
        grad=optimize.approx_fprime(xcur, f, e*e) #step2
    return xcur #step10

print(NR(startPointArr[2], stepArr[2], 0.01, f3, h3))