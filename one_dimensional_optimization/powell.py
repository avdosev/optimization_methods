import numpy as np

# Метод параболической аппроксимации Пауэлла
def powell(func, a: float, b: float, eps =0.01):
    # step 1
    x1 = a
    x2 = (a + b) / 2
    x3 = b

    X = [x1, x2, x3]
    # step 2
    while (True):
        min_x = X[0]
        for i in X:
            if (func(i)<func(min_x)):
                min_x = i
        
        # step 3
        num = (X[1] ** 2 - X[2] ** 2) * func(X[0]) + (X[2] ** 2 - X[0] ** 2) * func(X[1]) + (X[0] ** 2 - X[1] ** 2)* func(X[2])
        denum = (X[1] - X[2]) * func(X[0]) + (X[2] - X[0]) * func(X[1]) + (X[0] - X[1]) * func(X[2])
        X.append(0.5 * (num / denum))
        # step 4
        if(abs(X[3] - min_x) <= eps):
            break
        #step 5
        X.sort()

        #step 6
        max_x = 0
        for i in range(4):
            if (func(X[i])>func(X[max_x])):
                max_x = i
        X.pop(max_x)



 #step 7
    return X[-1]       

        

