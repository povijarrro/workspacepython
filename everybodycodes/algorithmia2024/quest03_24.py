#!python

from copy import deepcopy

def column(grid:list[list[int]],c:int)->list[int]:
    return [l[c] for l in grid]

def transpose(grid:list[list[int]])->list[list[int]]:
    return [column(grid,j) for j in range(len(grid[0]))]

def relevant_grid(grid:list[list[int]])->list[list[int]]:
    rg:list[list[int]] = deepcopy(grid)
    rg = transpose([c for c in transpose(rg) if sum(c)>0])
    rg = [r for r in rg if sum(r)>0]
    return rg

def updateable(grid:list[list[int]],level:int, diag:bool=False)->list[list[bool]]:
    m = len(grid)
    n = len(grid[0])
    upd = [[bool(a) for a in row] for row in grid]
    if not diag:
        upd = [[grid[i][j] == level and grid[i-1][j] == level and grid[i+1][j] == level and grid[i][j-1] == level and grid[i][j+1] == level for j in range(1,n-1)] for i in range(1,m-1)]
    else:
        upd = [[grid[i][j] == level and grid[i-1][j] == level and grid[i-1][j-1] == level and grid[i-1][j+1] == level and grid[i+1][j] == level and grid[i+1][j-1] == level and grid[i+1][j+1] == level and grid[i][j-1] == level and grid[i][j+1] == level for j in range(1,n-1)] for i in range(1,m-1)]
    upd.append([False for _ in range(len(upd[0]))])
    upd.insert(0,[False for _ in range(len(upd[0]))])
    upd = transpose(upd)
    upd.append([False for _ in range(len(upd[0]))])
    upd.insert(0,[False for _ in range(len(upd[0]))])
    upd = transpose(upd)
    return upd

def update_grid(grid:list[list[int]],diag:bool=False)->list[list[int]]:
    ug = deepcopy(grid)
    level = 2
    m = len(ug)
    n = len(ug[0])
    upd = updateable(ug,level-1,diag)
    upd_ug = [[ug[i][j] + upd[i][j] for j in range(n)] for i in range(m)]
    while(upd_ug != ug):
        ug = deepcopy(upd_ug)
        upd = updateable(ug,level,diag)
        upd_ug = [[ug[i][j] + upd[i][j] for j in range(n)] for i in range(m)]
        level+=1

    return upd_ug

def sol(grid:list[list[int]],diag:bool = False)->int:
    return sum([sum(r) for r in update_grid(relevant_grid(grid),diag)])


def main()->None:
    with open("./in03_24_1.txt") as inp:
        data:list[str] = inp.readlines()
        data = [d.strip() for d in data]
        grid1:list[list[int]] = [list(map(int,list(d.translate({ord("."):"0",ord("#"):"1"})))) for d in data]
    
    with open("./in03_24_2.txt") as inp:
        data:list[str] = inp.readlines()
        data = [d.strip() for d in data]
        grid2:list[list[int]] = [list(map(int,list(d.translate({ord("."):"0",ord("#"):"1"})))) for d in data]

    with open("./in03_24_3.txt") as inp:
        data:list[str] = inp.readlines()
        data = [d.strip() for d in data]
        grid3:list[list[int]] = [list(map(int,list(d.translate({ord("."):"0",ord("#"):"1"})))) for d in data]


    print(f"Part 1 : {sol(grid1,False)}\nPart 2 : {sol(grid2,False)}\nPart 3 : {sol(grid3,True)}")

if __name__ == "__main__":
    main()