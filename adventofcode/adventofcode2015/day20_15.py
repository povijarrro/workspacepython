#!python

import math

def divisors(n):
    divs = [i for i in range(1,int(math.sqrt(n) + 1)) if n % i == 0]

    return divs + [n // d for d in divs if d**2 != n]         

def elf_houses(elf:int)-> list:
    return [i*elf for i in range(1,51) ]

def house_elves(house:int, part = 1) -> list:
    divs = divisors(house)
    return [d for d in divs if house // d <= 50] if part != 1 else divs

def sol(minimal:int, part = 1)->int: 
    i=2
    
    while (10+(part != 1))*sum(house_elves(i,part))<minimal:
        i+=1

    return i
        
if __name__ == "__main__":
    
    minimal = 34000000
    print(f"Part 1 : {sol(minimal)}\nPart 2 : {sol(minimal,2)}")    