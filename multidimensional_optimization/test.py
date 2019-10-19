import unittest
import math
import importlib


import scipy
from scipy.optimize import minimize

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
        

class TestMultiVariableOptimization(unittest.TestCase):
    def test_coordinate_descense(self):
        from coordinate_descent import coordinate_descent

        fnc = lambda x1, x2: 4*(x1 - 5)**2 + (x2 - 6)**2

        def odm(fnc, x0, h):
            res = minimize(fnc, x0, method='nelder-mead',
                options={'xatol': h, 'disp': False})
            
            return res.x[0]

        res = coordinate_descent(fnc, 2, odm)
        print(res)
        eps = precision
        func_res = 0.
        self.assertTrue(abs(fnc(*res) - func_res) < eps)

    def test_hooke_jeeves(self):
        from HookeJeeves import HJ
        print("-----------------------")
        print("test_hooke_jeeves")
        print("-----------------------")
        eps = precision
        for i in range(len(funcsToTest)):
            print("\nTEST ", i+1 )
            res = HJ(startPoint[i],step[i],precision, funcsToTest[i])
            print("Получено:",  funcsToTest[i](res))
            print("Должно быть: ", func_res[i])
            print("Разница: ", funcsToTest[i](res) - func_res[i])
            self.assertAlmostEqual(func_res[i], funcsToTest[i](res), delta=eps)
            

    def test_fletcher_reeves(self):
        from FletcherReeves import FR
        print("-----------------------")
        print("test_fletcher_reeves")
        print("-----------------------")
        eps = precision
        for i in range(len(funcsToTest)):
            print("\nTEST ", i+1 )
            res = FR(startPoint[i],step[i],precision, funcsToTest[i])
            print("Получено:",  funcsToTest[i](res))
            print("Должно быть: ", func_res[i])
            print("Разница: ", funcsToTest[i](res) - func_res[i])
            self.assertAlmostEqual(func_res[i], funcsToTest[i](res), delta=eps)
            
if __name__ == '__main__':
    unittest.main()
        