# Бинарный поиск
def bin(a,b,e,d,f):
    while ((b-a)/2 >= e):
        x1 = (a+b)/2 - d
        x2 = (a+b)/2 + d
        if (f(x1)<=f(x2)):
            b = x2
        else:
            a = x1
    return (a+b)/2