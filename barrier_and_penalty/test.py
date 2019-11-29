def f1(x):
    x1,x2 = x
    return x1**2+x2**2

restrictionsOfEquality = [
    [lambda x1,x2: x1+x2-2],
    [],
    [lambda x1,x2: x1-1],
    [lambda x1,x2: x1-1],
    [],
    [],
    []
]

restrictionsOfNotEquality = [
    [],
    [lambda x1,x2: -x1+1,lambda x1,x2: x1+x2-2],
    [lambda x1,x2: x1+x2-2],
    [lambda x1,x2: x1+x2-2],
    [lambda x1,x2: -x1+1,lambda x1,x2: x1+x2-2],
    [lambda x1,x2: -x1+1,lambda x1,x2: x1+x2-2],
    [lambda x1,x2: -x1+1,lambda x1,x2: x1+x2-2]
]

startPoints = [
    [0., 0.],
    [2., -1.],
    [0., 1.],
    [2., 2.],
    [0., 1.],
    [2., 2.],
    [1., 1.]
]

funcsToTest = [
    f1,
    f1,
    f1,
    f1,
    f1,
    f1,
    f1
]

from barrier import *
from penalty import *

print("PENALTY METHOD: ")
for i in range(6):
    res = penalty(startPoints[i], 
        funcsToTest[i], 
        0.1, 
        10, 
        0.01,
        restrictionsOfEquality[i], 
        restrictionsOfNotEquality[i]
    )
    r = "".join([f"{j:.{5}f} " for j in res])
    print(f"{i}:", r) 

print("BARRIER METHOD: ")
for i in [1]:
    res = barrier(startPoints[i], 
        funcsToTest[i], 
        100, 
        0.5, 
        0.00625,
        restrictionsOfNotEquality[i]
    )
    r = "".join([f"{j:.{5}f} " for j in res])
    print(f"{i}:", r) 