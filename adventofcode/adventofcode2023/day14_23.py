#!python
from readLines import readLines
from day11_23 import getCol,getRow

def tiltedNorth(data:list[str])->list[str]:
    cdata=[]
    for j in range(len(data[0])):
        cdata.append(getCol(data,j))
    
    cdata = tiltedWest(cdata)
    cdata2=[]
    
    for j in range(len(cdata[0])):
        cdata2.append(getCol(cdata,j)) 
    
    return cdata2

def tiltedSouth(data:list[str])->list[str]:
    return tiltedNorth(data[::-1])[::-1]

def tiltedStrEast(s:str)->str:
    splited=s.split("#")
    tilted=splited.copy()
    for i,st in enumerate(splited):
        if st != "" : tilted[i]=st.count(".")*"."+st.count("O")*"O"
    
    tilted = [st+"#" for st in tilted]
    return "".join(tilted)[:-1]

def tiltedEast(data:list[str])->list[str]:
    tilted=[]
    for r in data:
        tilted.append(tiltedStrEast(r))

    return tilted 

def tiltedWest(data:list[str])->list[str]:
    tilted=[]
    for r in data:
        tilted.append(tiltedStrEast(r[::-1])[::-1])

    return tilted  

def cycledonce(data:list[str])->list[str]:
    north=tiltedNorth(data)
    west=tiltedWest(north)
    south=tiltedSouth(west)
    east=tiltedEast(south)

    return east

def cycled(data:list[str],times:int)->list[str]:
    cyc=cycledonce(data)
    for i in range(times-1):
        print(i)
        cyc=cycledonce(cyc)

    return cyc    

def solution1(data:list[str])->int:
    tdata=tiltedNorth(list(map(list,data)))
    n = len(data)
    sol= 0 
    for i in range(n):
        sol+=getRow(tdata,i).count("O")*(n-i)

    return sol

def solution2(data:list[str])->int:
    return(solution1(tiltedNorth(cycled(data,1000000000))))

if __name__ == "__main__":
    data = readLines("example14.txt")
    print(f"Part 1 : {solution1(data)}") 
    print(f"Part 2 : {solution2(data)}")