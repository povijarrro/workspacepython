#!python
from collections import Counter
from functools import reduce

def cprod(n):
    return reduce(lambda x,y:x*y,[int(i) for i in list(str(n))])

def test(n):
    i = n
    oldi = None
    res=[n]
    
    while(i != oldi):
        oldi = i
        i = i+cprod(i)
        if (i != oldi ):res.append(i)

    return res    

def isGood(n):
    nl =[int(i) for i in list(str(n))]
    lenn =len(nl)
    c = Counter(nl)
    return  reduce(lambda x,y:x+y,[c[i]*i**lenn for i in range(10)])==n       

n = 7
for i in range(10**(n-1),10**(n)):
    if isGood(i) : print(f"{i}")

