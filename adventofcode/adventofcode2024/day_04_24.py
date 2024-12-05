#!python
from itertools import product
import regex
def column(data:list[str],c:str)->str:
    return "".join([d[c] for d in data])

def  transpose(data:list[str])->list[str]:
    return [column(data,j) for j in range(len(data[0]))]

def diagonal(data:list[str], level:int)->list[str]:
    m:int = len(data)
    n:int = len(data[0])
    return ["".join(data[p[0]][p[1]]  for p in product(range(m),range(n)) if p[0]+p[1] == level),"".join(data[::-1][p[0]][p[1]] for p in product(range(m),range(n)) if p[0]+p[1] == level)[::-1]]

def diags(data:list[str])->list[str]:
    m:int = len(data)
    n:int = len(data[0])
    return sum([diagonal(data,level) for level in range(m+n-1)],start = [])


def xmas(s:str)->list[str]:
    return len(regex.findall("XMAS",s,overlapped=True))+len(regex.findall("SAMX",s,overlapped=True))

def part1(data:list[str])->int: 
    return sum(xmas(d) for d in data)+sum(xmas(d) for d in transpose(data))+sum(xmas(d) for d in diags(data))

def part2(data:list[str])->int:
    m:int = len(data)
    n:int = len(data[0])
    res:int = 0
    for i in range(1,m-1):
        for j in range(1,n-1):
            if data[i][j] != "A":
                continue
            else:
                if data[i-1][j-1] == "M" and data[i+1][j+1] == "S" and data[i-1][j+1] == "S" and data[i+1][j-1] == "M":
                    res += 1
                if data[i-1][j-1] == "M" and data[i+1][j+1] == "S" and data[i-1][j+1] == "M" and data[i+1][j-1] == "S":
                    res += 1    
                if data[i-1][j-1] == "S" and data[i+1][j+1] == "M" and data[i-1][j+1] == "S" and data[i+1][j-1] == "M":
                    res += 1
                if data[i-1][j-1] == "S" and data[i+1][j+1] == "M" and data[i-1][j+1] == "M" and data[i+1][j-1] == "S":
                    res += 1    
    return res

def main()->None:
    with open("./input04_24.txt") as inp:
        data = inp.read().strip().split("\n")
    
    print(f"Part 1 : {part1(data)}\nPart 2 : {part2(data)}") 

if __name__ == "__main__":
    main()