#!python

import math

def divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n // i)
    for divisor in reversed(large_divisors):
        yield divisor

def sol(minimal:int)->int: 
    i=2
    while sum(divisors(i))<minimal:
        i+=1

    return(i)    


if __name__ == "__main__":
    
    minimal = 3400000
    print(sol(minimal))