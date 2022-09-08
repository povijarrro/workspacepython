#!python

from fractions import Fraction as Fr
from math import factorial

def rectanglemethod(f,a,b,n=1):
    res=0
    delta=(b-a)/n
    if n==1:
        return (b-a)*f((a+b)/2)
    for i in range(n):
        res+=delta*f(a+delta*(2*i+1)/2)
    return res

def trapezoidmethod(f,a,b,n=1):
    
    delta=(b-a)/n
    res=delta*f(a)/2
    
    if n==1:
        return (b-a)*(f(a)+f(b))/2
    for i in range(1,n):
        res+=delta*f(a+i*delta)
    return res+delta*f(b)/2   

print(rectanglemethod(lambda x:x**3,Fr(3),Fr(5),99999))
print(trapezoidmethod(lambda x:x**3,Fr(3),Fr(5),99999))

    