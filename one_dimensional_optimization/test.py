import unittest
import math

def func_1(x):
    return 4*x**3 - 8*x**2 - 11*x + 5

def func_2(x):
    return x + 3/(x**2)

def func_3(x):
    return (x+2.5)/(4-x**2)

def func_4(x):
    return -math.sin(x) - (math.sin(3*x)/3)

def func_5(x):
    return -2*math.sin(x) - math.sin(2*x) - (2*math.sin(3*x)/3)

arr_of_func = [func_1, func_2,func_3,func_4,func_5]
minimization_point = [1,1,0,1.5,1.5]

class TestSingleVariableOptimization(unittest.TestCase):

    def test_passive_search(self):
        print("test_passive_search")
        from passive_search import passive_search
        for index in range(len(arr_of_func)):
            h = 2
            func = arr_of_func[index]
            point = minimization_point[index]
            min_index = passive_search(point-h, point+h, 20, func)
            min_value = func(min_index)

            print(f"x={min_index} y={min_value}")

    def test_method_devisa_svenna_campy(self):
        print("test_method_devisa_svenna_campy")
        from method_devisa_svenna_campy import search_local_min
        for index in range(len(arr_of_func)):
            func = arr_of_func[index]
            point = minimization_point[index]
            a,b = search_local_min(func, point)

            print(f"a={a} b={b}")
    
    
    def test_fib(self):
        from fib import metod_fib
        print("Fib test")
        lineSearch = [
            [0, 10],
            [0, 3],
            [0, 3],
            [-2, 2],
            [0, 3]
            #[0,5]
        ]
        expected = [1.833, 1.817, 0, 0.785, 0.785]
        for i, item in enumerate(lineSearch):
            print("\nTEST ", i+1)
            res = fib.metod_fib(arr_of_func[i], lineSearch[i][0], lineSearch[i][1], eps=0.01) # 0.001 вызовет рекурсивное зацикливание, не делай так

            print("Экспериментально:", res)
            print("Ожидаемо", expected[i])
            self.assertAlmostEqual(res, expected[i], places=3)  # после третьего знака не учитываем различие

        
if __name__ == '__main__':
    unittest.main()
        
