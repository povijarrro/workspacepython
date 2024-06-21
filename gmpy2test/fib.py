#!python
from timeit import Timer
import gmpy2
import numpy as np

def _gmpfib(n:int)->gmpy2.mpz:
    Q = np.matrix([[gmpy2.mpz(1),gmpy2.mpz(1)],[gmpy2.mpz(1),gmpy2.mpz(0)]],dtype = object)
    if n > 1:
        Qn = Q**(n-1)
        return Qn[0,0]
    return gmpy2.mpz(n)

def _fib(n:int)->int:
     Q = np.matrix([[1,1],[1,0]],dtype = object)
     if n > 1:
         Qn = Q**(n-1)
         return Qn[0,0]
     return n

def gmpfib(n:int)->gmpy2.mpz:
    return (-1)**(-n-1)*_gmpfib(-n) if n < 0 else _gmpfib(n)
    
def fib(n:int)->int:
    return  (-1)**(-n-1)*_fib(-n) if n < 0 else _fib(n)
 
def main():
    #t = Timer(stmt = "fib(10_000_000)",setup = "from __main__ import fib")
    #print(f"without gmp : {t.timeit(1)}")
    #t = Timer(stmt = "gmpfib(10_000_000)",setup = "from __main__ import gmpfib")
    #print(f"with gmp : {t.timeit(10)/10}")
    #t = Timer(stmt = "gmpy2.fib(1_000_000_000)",setup = "import gmpy2")
    #print(f"from gmpy2 module : {t.timeit(1)}")
    f = gmpy2.fib(1_000_000_000)
    print(gmpy2.num_digits(f))
    
if __name__ == "__main__":
    main()