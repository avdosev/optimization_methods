class FibonacciImpl:
    arr = [0,1,1]

    def calculate(self, num: int):
        if num < len(self.arr):
            return self.arr[num]
        else:
            for i in range(len(self.arr)-1, num):
                new_fib = self.arr[i-1] + self.arr[i]
                self.arr.append(new_fib)
            return self.arr[num]

fib_impl = FibonacciImpl()

def fib(num):
    global fib_impl
    return fib_impl.calculate(num)

def metod_fib(func, a, b, eps=0.001, sigma=0.001 / 10):
    N = int((b - a) / (2 * eps))
    print('tyt N - ',N)
    x1 = a + fib(N - 2) / fib(N) * (b - a)
    x2 = a + fib(N - 1) / fib(N) * (b - a)
    for k in range(2, N - 2):
        if func(x1) <= func(x2):
            b = x2
            x2 = x1
            x1 = a + fib(N - k - 3) / fib(N - k - 1) * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + fib(N - k - 2) / fib(N - k - 1) * (b - a)
    x2 = x1 + sigma
    if func(x1) <= func(x2):
        b = x2
    else:
        a = x1
    return (a + b) / 2