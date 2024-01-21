#!python
from readLines import readLines

def getNums(data):
    numstr=[]
    
    for i,line in enumerate(data):
        num=""
        coords=()
        for j,c in enumerate(line):
            if(c.isdigit()):
                if not num:coords=(i,j)
                num += c
                if j == len(line)-1:
                    numstr.append((num,(i,j-len(num)+1)))
                    num=""
                    coords=()
            else:
                if num:numstr.append((num,coords))
                num=""
                coords=()
        num=""        

    return numstr 

def neighbours(i,j,dim):
    nb=[]
    for k in [-1,0,1]:
        for l in [-1,0,1]:
            nb.append((i+k,j+l))

    nb =list(filter(lambda a:0<=a[0]<=dim[0]-1 and 0<=a[1]<=dim[1]-1 and a!=(i,j),nb))      
    return nb

def hasNumNeighbour(data, i, j):
    for nb in neighbours(i,j,(len(data),len(data[0]))):
        if(data[nb[0]][nb[1]].isdigit) : return True
    
    return False
              

def getSymbols(data):
    symbs=[]
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (hasNumNeighbour(data,i,j) and (not data[i][j].isdigit()) and data[i][j]!="."):
                symbs.append((data[i][j],(i,j)))

    return symbs
 
def f(a):
    data=readLines("example03.txt")
    n = len(data)
    m = len(data[0])
    symbs = getSymbols(data)
    
    for _,coord in symbs:
        for i in range(len(a[0])):
            if coord in neighbours(a[1][0],a[1][1]+i,(n,m)):
                return True

    return False

def numNeighbours(i,j,data):
    neighs=[]
    nums =getNums(data)
    for num,coords in nums:
        for k in range(len(num)):
            if (i,j) in neighbours(coords[0],coords[1]+k,(len(data),len(data[0]))):
                neighs.append(num)
                break    
        
    return neighs


def solution1(data):
    nums = getNums(data)
    nums = list(filter(f,nums))
    return sum([int(i[0])for i in nums])

def solution2(data):
    symbs = getSymbols(data)

    l=list(filter(lambda a:a[0]=="*" and len(numNeighbours(a[1][0],a[1][1],data))==2,symbs))
    
    l=[int(numNeighbours(i[1][0],i[1][1],data)[0])*int(numNeighbours(i[1][0],i[1][1],data)[1]) for i in l]

    return sum(l)



if __name__ == "__main__":
    data = readLines("example03.txt")
    
    print(f"Part 1 : {solution1(data)}")
    print(f"Part 2 : {solution2(data)}")
    