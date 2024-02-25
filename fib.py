#!python
import sys
from timeit import timeit
def fib_rec(n):
    if n in (0, 1):
        return n
    else:
        return fib_rec(n-2) + fib_rec(n-1)

        
def _fib(n):
    if n == 0:
        return (0, 1)
    else:
        a, b = _fib(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

def fib(n):
    return _fib(n)[0]              

sys.set_int_max_str_digits(0)
for i in range(1000000):
    print(f"{1000*i} : {timeit(lambda:fib(1000*i))}")