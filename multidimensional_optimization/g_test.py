import pylab
import numpy as np
import matplotlib.pyplot as plt

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

def makeData(fun):
    xstart = -5
    xend = 5
    ystart = -5
    yend = 5
    # eps = 0.05
    # x = numpy.arange(xstart, xend, eps)
    # y = numpy.arange(ystart, yend, eps)
    div = 100
    x=np.linspace(xstart,xend,div) 
    y=np.linspace(ystart,yend,div)
    xgrid, ygrid = np.meshgrid(x, y)
    zgrid = np.empty([div, div])
    for j in range(0, len(x)):
        for i in range(0, len(y)):
            zgrid[i][j]=fun([x[j],y[i]])
    

    # zgrid = []
    # for x,y in xr,yr:
    #     zgrid.append(fun([x,y]))
    # zgrid = np.array(zgrid)    

    return xgrid, ygrid, zgrid

import FletcherReeves

funcsToTest = [f1, f2,f3,f4] 
startPoint = [[0.,0.],[0.,0.],[0.,0.,0.,0.],[1.,1.,1.,1.]]
step = [[1.,1.],[1.,1.],[1.,1.,1.,1.],[1.,1.,1.,1.]]
precision = 0.01
func_res = [0.,0.,0.,0.]

if __name__ == '__main__':
    lev = [1, 5, 10, 25, 50, 100, 200]
    x, y, z = makeData(f2)

    fig, axes = plt.subplots(1,1)
    axes.contour(x, y, z, levels = lev, colors='k')

    res = FletcherReeves.FR(startPoint[0], step[0], 0.01, funcsToTest[1])
    testP = FletcherReeves.FRPath

    for point in testP:
        plt.scatter(point[0], point[1], c='r', s=2,)

    print(res)
    plt.show()