def f1(x):
    x1,x2 = x
    return x1**2+x2**2

restrictionsOfEquality = [
    [[1,1,-2]],
    [[1,1,-2]],
    [[1,0,-1]],
    [[1,0,-1]],
    [],
    []
]

restrictionsOfNotEquality = [
    [],
    [],
    [[1,1,-2]],
    [[1,1,-2]],
    [[-1,0,1],[1,1,-2]],
    [[-1,0,1],[1,1,-2]]
]

startPoints = [
    [0,0],
    [2,2],
    [0,1],
    [2,2],
    [0,1],
    [2,2]
]

funcsToTest = [
    f1,
    f1,
    f1,
    f1,
    f1,
    f1
]

import barrier
import penalty

res = penalty.penalty(startPoints[0], 
funcsToTest[0], 
0.1, 
10, 
0.01,
restrictionsOfEquality[0], 
restrictionsOfNotEquality[0])
print(res)