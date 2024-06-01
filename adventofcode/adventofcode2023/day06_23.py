#!python
from functools import reduce
from readLines import readLines

def distance(time:int,hold:int)->int:
    return hold*(time-hold)

def  nOfRecords(time:int, oldrec:int)->int:
    n=0
    for i in range(time+1):
        if distance(time,i)>oldrec:n+=1

    return n

def solution1(data:list[list[str]])->int:
    times = [int(i) for i in data[0]]
    oldrecs =[int(i) for i in data[1]]
    recs=[]

    for i, time in enumerate(times):
        recs.append(nOfRecords(time,oldrecs[i]))
    
    return reduce(lambda a,b:a*b,recs)

def solution2(data:list[list[str]])->int:
    time = int("".join(data[0]))
    rec = int("".join(data[1]))
    
    return nOfRecords(time,rec)
    

def main():
    data = readLines("input06_23.txt")
    data = [i.split()[1:] for i in data]
    
    print(f"Part 1 : {solution1(data)}")
    print(f"Part 2 : {solution2(data)}")

if __name__ == "__main__":
    main()