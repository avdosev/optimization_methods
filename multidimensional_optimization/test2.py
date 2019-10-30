import math
import importlib
import scipy
from scipy.optimize import minimize

from FletcherReeves import FR
from HookeJeeves import HJ

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

funcsToTest = [f1, f2,f3,f4] 
startPoint = [[0.,0.],[0.,0.],[0.,0.,0.,0.],[1.,1.,1.,1.]]
step = [[1.,1.],[1.,1.],[1.,1.,1.,1.],[1.,1.,1.,1.]]
precision = 0.01
func_res = [0.,0.,0.,0.]
 
def test(funToTest, text):
    print("-----------------------")
    print("test:"+text)
    print("-----------------------")
    eps = precision
    for i in range(len(funcsToTest)):
        print("\nTEST ", i+1 )
        res = FR(startPoint[i],step[i],precision, funcsToTest[i])
        print("Получено:",  funcsToTest[i](res))
        print("Должно быть: ", func_res[i])
        print("Разница: ", funcsToTest[i](res) - func_res[i])

test(FR, "FletcherReeves")
test(FR, "HookeJeeves")
