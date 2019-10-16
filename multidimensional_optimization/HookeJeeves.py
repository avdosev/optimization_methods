machineAcc = 0.000000001

#2.1.2.2
# Исследующий поиск
def utilSearch(b, h, f):
    bres = b[:]
    fb = f(bres)
    for i in range(0,len(bres)):
        bn = bres
        bn[i] = bn[i] + h[i]     
        fc = f(bn)
        if (fc + machineAcc<fb):
            bres = bn
            fb = fc
        else:
            bn[i] = bn[i] - 2*h[i]
            fc = f(bn)
            if (fc + machineAcc < fb):
                bres = bn
                fb = fc
    return bres

#2.1.2.1
# Метод конфигураций Хука-Дживса
# Находит минимум многомерной функции
def HJ(b1, h, e, f):
    z = 0.1
    runOuterLoop = True
    while (runOuterLoop):
        runOuterLoop = False
        runInnerLoop = True
        xk = b1 #step1
        b2 = utilSearch(b1, h, f) #step2
        while (runInnerLoop):
            runInnerLoop = False
            for i in range(len(b1)):#step3
                xk[i] = b1[i] + 2*(b2[i]-b1[i])
            x = utilSearch(xk, h, f) #step4
            b1 = b2 #step5
            fx = f(x)
            fb1 = f(b1)
            if (fx+machineAcc<fb1): #step6
                b2 = x
                runInnerLoop = True #to step3
            elif (fx-machineAcc>fb1): #step7
                runOuterLoop = True #to step1
                break
            else:
                s = 0 
                for i in range(len(h)):
                    s+=h[i]*h[i]
                if (e*e + machineAcc > s): #step8
                    break #to step10
                else:
                    for i in range(len(h)): #step9
                        h[i] = h[i]* z 
                    runOuterLoop = True #to step1
    return b1 #step10

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

funcToTest = f1
startPoint = [0.,0.]
step = [1.,1.]
precision = 0.01
res = HJ(startPoint,step,precision, funcToTest)
print(res)
print(funcToTest(res))