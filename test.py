def f1(x):
    x1,x2 = x
    return x1**2+x2**2

restrictionsOfEquality = [
    [lambda x1,x2: x1+x2-2],
    [lambda x1,x2: x1+x2-2],
    [lambda x1,x2: x1-1],
    [lambda x1,x2: x1-1],
    [],
    [],
    []
]

restrictionsOfNotEquality = [
    [],
    [],
    [lambda x1,x2: x1+x2-2],
    [lambda x1,x2: x1+x2-2],
    [lambda x1,x2: -x1+1,lambda x1,x2: x1+x2-2],
    [lambda x1,x2: -x1+1,lambda x1,x2: x1+x2-2],
    [lambda x1,x2: -x1+1,lambda x1,x2: x1+x2-2]
]

startPoints = [
    [0,0],
    [2,2],
    [0,1],
    [2,2],
    [0,1],
    [2,2],
    [1,1]
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

import barrier
import penalty

# print("PENALTY METHOD: ")
# for i in range(6):
#     res = penalty.penalty(startPoints[i], 
#     funcsToTest[i], 
#     0.1, 
#     10, 
#     0.01,
#     restrictionsOfEquality[i], 
#     restrictionsOfNotEquality[i])
#     print(f"{i}:") 
#     r = ""
#     for j in res:
#         r+=f"{j:.{5}f} "
#     print(r)

# print("BARRIER METHOD: ")
# for i in [6]:
#     res = barrier.barrier(startPoints[i], 
#     funcsToTest[i], 
#     100, 
#     0.5, 
#     0.0625,
#     restrictionsOfNotEquality[i])
#     print(f"{i}:") 
#     r = ""
#     for j in res:
#         r+=f"{j:.{5}f} "
#     print(r)


print("BARRIER METHOD: ")
res = barrier.barrier([2,-1], 
f1, 
100, 
0.5, 
0.005,
restrictionsOfNotEquality[6])
r =""
for j in res:
    r+=f"{j:.{5}f} "
print(r)