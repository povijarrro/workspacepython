import math
import datetime
def fibonacci_rec(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci_rec(n-2) + fibonacci_rec(n-1)


def fib_gen():
    yield 0
    a, b = 0, 1
    while(True):
        a, b = b, a+b
        yield a

def fibonacci(n):
    fibgen = fib_gen()
    if n < 0:
        c = 1 if n%2 else -1
        return c*fibonacci(-n)
    i = 0
    for f in fibgen:
        if i == n:
            return f
        i += 1
        
def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2    

print(fib(1000000))