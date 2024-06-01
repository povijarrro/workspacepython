#!python
from readLines import readLines

def noGalaxies(rc:str)->bool:
    return rc.count(".")==len(rc)

def getRow(data:list[str],i:int)->str:
    if i in range(len(data)):
        return data[i]
    return None

def getCol(data:list[str],j:int)-> str:
    if j in range(len(data[0])):
        col = []
        for d in data:
            col.append(d[j])
        return "".join(col)
    return None

def insertCol(data:list[str],col:str,j:int)->None:
    for i in range(len(data)):
        data[i]=data[i][:j]+col[i]+data[i][j:]
    
def incData(data:list[str],speed:int)->list[str]:
    newData=data.copy()
    newData2=newData.copy()
    count=0
    for i in range(len(data)):
        if noGalaxies(getRow(data,i)):
            for _ in range(speed-1):
                newData.insert(i+count,data[i])
                count+=1
    
    newData2=newData.copy()
    
    count=0
    for j in range(len(newData[0])):
        col =getCol(newData,j)
        if noGalaxies(col):
            for _ in range(speed-1):
                insertCol(newData2,col,j+count)
                count+=1
                  
    return newData2  

def offset(data:list[str], speed:int, coords:tuple)->tuple:
    off0=0
    off1=0

    for i in range(coords[0]):
        if noGalaxies(data[i]):off0+=speed-1
    
    for j in range(coords[1]):
        if noGalaxies(getCol(data,j)):off1+=speed-1
 
    return (off0,off1)

def getCoords(data:list[str])->list[tuple]:
    coords=[]
    for i,d in enumerate(data):
        for j,ch in enumerate(d):
            if ch=="#":coords.append((i,j))   

    return coords          

def getPathLen(start:tuple,end:tuple)->int:
    return abs(end[0]-start[0])+abs(end[1]-start[1])  

def solution1(data:list[str])->int:
    coords = getCoords(data)
    for i,coo in enumerate(coords[:]):
        off = offset(data,2,coo)
        coords[i]=(coo[0]+off[0],coo[1]+off[1])
   
    sum=0
    for i in range(len(coords)):
        for j in range(i,len(coords)): 
            sum+=getPathLen(coords[i],coords[j])    
    
    return sum

def solution2(data:list[str])->int:
    coords = getCoords(data)
    for i,coo in enumerate(coords[:]):
        off = offset(data,1000000,coo)
        coords[i]=(coo[0]+off[0],coo[1]+off[1])

    sum=0
    for i in range(len(coords)):
        for j in range(i,len(coords)): 
            sum+=getPathLen(coords[i],coords[j])   
    
    return sum

def main():
    data = readLines("input11_23.txt")
    
    print(f"Part 1 : {solution1(data)}")
    print(f"Part 2 : {solution2(data)}")

if __name__ == "__main__":
    main()