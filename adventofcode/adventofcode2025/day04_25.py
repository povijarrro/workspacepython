#!python
from copy import deepcopy


def neighbours(point:tuple[int,int],data:list[str])->set[tuple[int,int]]:
    
    res = set()
    m = len(data)
    n = len(data[0]) 
    
    for a in [-1,0,1]:
        for b in [-1,0,1]:
            res.add((min(max(point[0]+a,0),m-1),min(max(point[1]+b,0),n-1)))
    
    res.remove(point)
    
    return res        

def update_data(data:list[str], recursive:bool=False)->list[str]:
    
    papers = 0
    newdata = [list(s) for s in data]
    
    for i,s in enumerate(data):
        for j,c in enumerate(s):
            if c == "@" and sum(data[k][l] == "@" for (k,l) in neighbours((i,j),data))<4:
                papers += 1 
                newdata[i][j]="."

    newdata = ["".join(s) for s in newdata]  
    
    if not recursive:
        return newdata,papers 
    else:
        if newdata == data:
            return newdata,0
        else:
            ud = update_data(newdata,True)
            return ud[0],papers+ud[1]


def sol(data:list[str], part:int = 1):
    return update_data(data,part == 2)[1]
    
def main()->None:
    with open("input04_25.txt") as inp:
        data = [d.strip() for d in inp.readlines()]

    print(f"Part 1 : {sol(data,1)}\nPart 2 : {sol(data,2)}")    

if __name__ == "__main__":
    main() 