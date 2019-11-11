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


Path1 = []
Path2 = []
Path3 = []
Path4 = []

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
        Path1.append(b1)
        Path2.append(b2)
        Path3.append(xk)
        while (runInnerLoop):
            Path1.append(b1)
            Path2.append(b2)
            runInnerLoop = False
            for i in range(len(b1)):#step3
                xk[i] = b1[i] + 2*(b2[i]-b1[i])
            Path3.append(xk)
            x = utilSearch(xk, h, f) #step4
            Path4.append(x)
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