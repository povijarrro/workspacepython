#!python
from copy import deepcopy
import sys

sys.setrecursionlimit(10000000)

def path(data:list[list[str]],start:tuple[int,int])->list[tuple[int,int]]:
    pth:list[tuple[int,int]] = [start]
    pos:tuple[int,int] = start
    d:list[str] = data
    
    if d[pos[0]][pos[1]] == "^":
        i:int = pos[0]-1
        while i>=0:
            if d[i][pos[1]] == ".":
                pth.append((i,pos[1])) 
            else:
                break     
            i-=1
        i = pth[-1][0]
        d[i][pos[1]] = ">"
        d[start[0]][start[1]]= "."
        if i == 0:
            return  pth
        else:
            pth.extend(path(d,(i,pos[1]))[1:])
            return pth

    if d[pos[0]][pos[1]] == ">":
        j:int = pos[1]+1
        while j<len(d[0]):
            if d[pos[0]][j] == ".":
                pth.append((pos[0],j))
            else:
                break    
            j += 1
        j = pth[-1][1]
        d[pos[0]][j] = "v"
        d[start[0]][start[1]]= "."
        if j == len(d[0])-1:
            return  pth
        else:
            pth.extend(path(d,(pos[0],j))[1:])
            return pth
        
    if d[pos[0]][pos[1]] == "v":
        i:int = pos[0]+1
        while i<len(d):
            if d[i][pos[1]] == ".":
                pth.append((i,pos[1])) 
            else:
                break     
            i += 1
        i = pth[-1][0]
        d[i][pos[1]] = "<"
        d[start[0]][start[1]]= "."
        if i == len(d)-1:
            return  pth
        else:
            pth.extend(path(d,(i,pos[1]))[1:])
            return pth    
        
    if d[pos[0]][pos[1]] == "<":
        j:int = pos[1]-1
        while j>0:
            if d[pos[0]][j] == ".":
                pth.append((pos[0],j)) 
            else:
                break     
            j -= 1
        j = pth[-1][1]
        d[pos[0]][j] = "^"
        d[start[0]][start[1]]= "."
        if j == len(d[0])-1:
            return  pth
        else:
            pth.extend(path(d,(pos[0],j))[1:])
            return pth    
    
    return pth
def part1(data:list[list[str]])->int:
    m:int = len(data)
    n:int = len(data[0])
    start:tuple[int,int] = [(i,j) for i in range(m) for j in range(n) if data[i][j] in {"^",">","v",">"}][0]
    pth:list[tuple[int,int]] = path(data,start)
    return len(set(pth))

def part2(data:list[list[str]])->int:
    pass

def main()->None:
    with open("./input06_24.txt") as inp:
        data = [list(d) for d in inp.read().strip().split("\n")]

    with open("./example06_24.txt") as inp:
        ex = [list(d) for d in inp.read().strip().split("\n")]  
    
    print(part1(ex))
    #print(f"Part 1 : {part1(data)}\nPart 2 : {part2(data)}")
    
if __name__ == "__main__":
    main()