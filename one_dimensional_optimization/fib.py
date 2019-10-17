class FibonacciImpl:
    arr = [0, 1, 1]

    def fib(self, num: int):
        if num < len(self.arr):
            return self.arr[num]
        else:
            new_fib = self.fib(num - 2) + self.fib(num - 1)
            self.arr.append(new_fib)
            return new_fib

    def metod_fib(self, func, a, b, eps=0.001, sigma=0.001 / 10):
        N = int((b - a) / (2 * eps))
        x1 = a + self.fib(N - 2) / self.fib(N) * (b - a)
        x2 = a + self.fib(N - 1) / self.fib(N) * (b - a)
        for k in range(2, N - 2):
            if func(x1) <= func(x2):
                b = x2
                x2 = x1
                x1 = a + self.fib(N - k - 3) / self.fib(N - k - 1) * (b - a)
            else:
                a = x1
                x1 = x2
                x2 = a + self.fib(N - k - 2) / self.fib(N - k - 1) * (b - a)
        x2 = x1 + sigma
        if func(x1) <= func(x2):
            b = x2
        else:
            a = x1
        return (a + b) / 2