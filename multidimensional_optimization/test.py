import unittest
import math
import importlib


import scipy
from scipy.optimize import minimize

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

class TestMultiVariableOptimization(unittest.TestCase):
    def test_coordinate_descense(self):
        from coordinate_descent import coordinate_descent

        fnc = lambda x1, x2: 4*(x1 - 5)**2 + (x2 - 6)**2

        def odm(fnc, x0, h):
            res = minimize(fnc, x0, method='nelder-mead',
                options={'xtol': h, 'disp': False})
            
            return res.x[0]

        res = coordinate_descent(fnc, 2, odm)
        print(res)
        eps = 0.001
        self.assertEqual(abs(fnc(*res) - eps) < eps, True)

    def test_hooke_jeeves(self):
        from HookeJeeves import HJ
        funcToTest = f1
        startPoint = [0.,0.]
        step = [1.,1.]
        precision = 0.01
        res = HJ(startPoint,step,precision, funcToTest)
        print(res)
        print(funcToTest(res))
        pass

    def test_fletcher_reeves(self):
        from FletcherReeves import FR
        funcToTest = f1
        startPoint = [0.,0.]
        step = [1.,1.]
        precision = 0.01
        res = FR(startPoint,step,precision, funcToTest)
        print(res)
        print(funcToTest(res))
        
if __name__ == '__main__':
    unittest.main()
        