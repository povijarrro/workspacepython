#!python

import sympy
import z3


if __name__ == "__main__":
    a = [[1,2],[3,4]]
    x,y=z3.Reals("x y")
    expr = z3.eq((x+y)**2,x**2+2*x*y+y**2)
    sympy.pprint(expr)
    print(expr)