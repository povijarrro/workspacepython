#!python
from math import lcm
from readLines import readLines

def findIndex(data:list[dict],key:str)->int:
    for i,d in enumerate(data):
        if key in d.keys():return i

def getDest(start:str,data:dict,dir:str)->str:
    if dir=="L":return data[start][0]
    else: return data[start][1]      

def getPath(start:str,end:str,data:dict,navs:str)->list[str]:
    dest=start
    n=len(navs)
    path=[]
    i=0
    while dest != end:
        if navs[i]=="L":
            dest=data[dest][0]
            if dest==end:
                path.append(end)
                return path
        else:
            dest=data[dest][1]
            if dest == end:
                path.append(end)
                return path

        path.append(dest)
        i=(i+1)%n
        
    return path

def getPath2(start:str,data:dict,navs:str)->list[str]:
    dest=start
    n=len(navs)
    path=[]
    i=0
    while not dest.endswith("Z"):
        if navs[i]=="L":
            dest=data[dest][0]
            if dest.endswith("Z"):
                path.append(dest)
                return path
        else:
            dest=data[dest][1]
            if dest.endswith("Z"):
                path.append(dest)
                return path

        path.append(dest)
        i=(i+1)%n
        
    return path

def solution1(data:list[dict], navs:str)->int:
    return len(getPath("AAA", "ZZZ", data,navs))

def solution2(data:dict, navs:str)->int:
    starts=[start for start in data.keys() if start.endswith("A")]
    pathLens=[]
    for start in starts:
        pathLens.append(len(getPath2(start, data, navs)))
            
    return lcm(*pathLens)

def main():
    data = readLines("input08_23.txt","\n\n")
    navs, *data = data
    data = [i.split("\n") for i in data][0]
    
    d=dict()
    for da in data:
        spl=da.split(" = ")
        d[spl[0]]=(spl[1].split(", ")[0][1:],spl[1].split(", ")[1][:-1])

    data = d
    
    print(f"Part 1 : {solution1(data,navs)}")
    print(f"Part 2 : {solution2(data,navs)}")

if __name__ == "__main__":
    main()    
    