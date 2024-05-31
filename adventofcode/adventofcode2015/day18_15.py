#!python

def neighbours(i:int,j:int,dim:tuple[int,int])->list[tuple[int,int]]:
    nb=[]
    for k in [-1,0,1]:
        for l in [-1,0,1]:
            nb.append((i+k,j+l))

    nb =list(filter(lambda a:0<=a[0]<=dim[0]-1 and 0<=a[1]<=dim[1]-1 and a!=(i,j),nb))
    return nb

def update(data:list[list[int]],corner_stuck=False)->list[list[int]]:
    new = [d[:] for d in data[:]]
    dim = len(data),len(data[0])
        
    for i in range(dim[0]):
        for j in range(dim[1]):
            num_on_neighs = sum(data[nb[0]][nb[1]] for nb in neighbours(i,j,dim)) 
            if not corner_stuck:
                if data[i][j]:new[i][j]=int(2<=num_on_neighs<=3)
                else:new[i][j]=int(num_on_neighs==3) 
            else:
                if (i,j) in [(0,0),(0,dim[1]-1),(dim[0]-1,0),(dim[0]-1,dim[1]-1)]:new[i][j]=1
        
                else:
                    if data[i][j]:new[i][j]=int(2<=num_on_neighs<=3)
                    else:new[i][j]=int(num_on_neighs==3) 
                    

    return new

def sol(data:list[list[int]],part=1)->list[list[int]]:
    
    new = [d[:] for d in data[:]]

    for _ in range(100):
        new = update(new,part!=1)
    
    return sum(sum(d) for d in new)  


def main() :
    with open("input18_15.txt") as inp:
        data=[list(d.strip()) for d in inp.readlines()]
        data=[[0 if c=="." else 1 for c in s] for s in data]

    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")

if __name__ == "__main__":
    main()    