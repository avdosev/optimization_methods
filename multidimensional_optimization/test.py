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

def f5(x):
    x, y = x
    return (0.1*x**2) + (0.1*y**2) - 4*math.cos(0.8*x) - 4*math.cos(0.8*y) + 8

def f6(x):
    x, y = x
    return (-0.15*y)**2 + (0.08*x)**2 - 4*math.cos(-1.2*y) - 4*math.cos(0.64*x) + 8

def f7(x):
    x, y = x
    return -10/(0.005*(x**2+y**2)-math.cos(x)*math.cos(y/1.41421356237309504880168)+2)+10




funcsToTest = [f1, f2, f3, f4, f5, f6] 
startPoint = [[0.,0.],[0.,0.],[0.,0.,0.,0.],[1.,1.,1.,1.], [1., 1.], [1., 1.]]
step = [[1.,1.],[1.,1.],[1.,1.,1.,1.],[1.,1.,1.,1.], [1., 1.], [1., 1.]]
precision = 0.01
func_res = [0.,0.,0.,0.,0.,0.]
        
def test_function(self, method_name, test_fnc):
    print("-----------------------")
    print(method_name)
    print("-----------------------")
    eps = precision
    for i in range(len(funcsToTest)):
        print("\nTEST ", i+1 )
        res = test_fnc(i)
        print("Точки:", res)
        print("Получено:",  funcsToTest[i](res))
        print("Должно быть: ", func_res[i])
        print("Разница: ", funcsToTest[i](res) - func_res[i])
        # self.assertAlmostEqual(func_res[i], funcsToTest[i](res), delta=eps)

class TestMultiVariableOptimization(unittest.TestCase):
    def test_coordinate_descense(self):
        from coordinate_descent import coordinate_descent

        def odm(fnc, x0, h):
            res = minimize(fnc, x0, method='nelder-mead',
                options={'xatol': h, 'disp': False})
            return res.x[0]

        test_function(self, "coordinate_descense",
            lambda i: coordinate_descent(lambda *args: funcsToTest[i](args), startPoint[i], odm)
        )

    def test_hooke_jeeves(self):
        from HookeJeeves import HJ
        test_function(self, "test_hooke_jeeves",
            lambda i: HJ(startPoint[i],step[i],precision, funcsToTest[i])
        )
            

    def test_fletcher_reeves(self):
        from FletcherReeves import FR
        test_function(self, "test_fletcher_reeves", 
            lambda i: FR(startPoint[i],step[i],precision, funcsToTest[i])
        )

    def test_optimal_gradient(self):
        from optimal_gradient_method import optimal_gradient_method
        test_function(self, "optimal_gradient_method", 
            lambda i: optimal_gradient_method(funcsToTest[i], startPoint[i])
        )

    def test_adaptive_method(self):
        from stochastic.adaptive_method import adaptive_method
        test_function(self, "adaptive_method", 
            lambda i: adaptive_method(funcsToTest[i], startPoint[i], 1000, 100)
        )

    def test_boltzman_method(self):
        from stochastic.boltzmann_method import boltzmann_method
        test_function(self, "boltzman_method", 
            lambda i: boltzmann_method(startPoint[i], 1., funcsToTest[i], 100000)
        )

    def test_best_samples_method(self):
        from stochastic.best_samples import best_samples
        test_function(self, "best_samples_method",
            lambda i: best_samples(funcsToTest[i], startPoint[i], 150, 500, 1, 0.0001, 0.1)
        )

            
if __name__ == '__main__':
    unittest.main()
        