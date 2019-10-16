import unittest
import math
import importlib

from coordinate_descent import coordinate_descent

import scipy
from scipy.optimize import minimize

class TestMultiVariableOptimization(unittest.TestCase):
    def test_coordinate_descense(self):

        fnc = lambda x1, x2: 4*(x1 - 5)**2 + (x2 - 6)**2

        def odm(fnc, x0, h):
            res = minimize(fnc, x0, method='nelder-mead',
                options={'xtol': h, 'disp': True})
            

            return res.x[0]

        res = coordinate_descent(fnc, 2, odm)

        print(res)

        pass
        
if __name__ == '__main__':
    unittest.main()
        