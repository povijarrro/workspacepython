#!python
from day11_23 import getRow,getCol
from readLines import readLines

def href(data:list[str])->int:
    for i in range(len(data)-1):
        ref=True
        for j in range(min(i,len(data)-2-i)+1):
            if getRow(data, i-j)!=getRow(data, i+1+j):
                ref=False
                break
        if ref: return i+1
 
    return -1
    
def vref(data:list[str])->int:
    for i in range(len(data[0])-1):
        ref=True
        for j in range(min(i,len(data[0])-2-i)+1):
            if getCol(data, i-j)!=getCol(data, i+1+j):
                ref=False
                break
        if ref: return i+1
    
    return -1 

def solution1(data:list[list[str]])->int:
    sol = 0
    for d in data:
        h=href(d)
        if h>= 0:
            sol+=100*h
            print(f"h : {h}")
        else:
            v = vref(d)
            if v>=0 : 
                sol+=v
                print(f"v : {v}")

    return sol
   

if __name__ == "__main__":
    data = readLines("input13.txt","\n\n")
    data = [d.splitlines() for d in data]
    print(solution1(data))
    

    