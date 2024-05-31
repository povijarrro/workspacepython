#!python

from itertools import product


def get_ngrid(plans:list[list[tuple]])->list[list[int]]:
    grid = []
    dim = max(plan[0][0]+plan[1][0] for plan in plans),max(plan[0][1]+plan[1][1] for plan in plans)
    for _ in range(dim[0]):
        row = []
        for _ in range(dim[1]):
            row.append(0)
        grid.append(row)    
    for plan in plans:
        for i in range(plan[0][0],plan[0][0]+plan[1][0]):
            for j in range(plan[0][1],plan[0][1]+plan[1][1]):
                grid[i][j]+=1
    return grid

def overlaps(i:int,j:int,plans)->bool:
    p_i = [plan for plan in plans if plan[2] == i][0]
    p_j = [plan  for plan in plans if plan[2] == j][0]
    return None

def sol(plans:list[list[tuple]],part = 1)->int:
    if part == 1:
        grid = get_ngrid(plans)
        m,n = len(grid),len(grid[0])
        return sum(grid[pos[0]][pos[1]]>1 for pos in product(range(m),range(n)))

def main():
    with open("input03_18.txt") as inp:
        plans = [d.strip().split(" @ ")[1].split(": ") for d in inp.readlines()]
        plans = [[tuple(map(int,plan[0].split(","))),tuple(map(int,plan[1].split("x")))] for plan in plans]
        plans = [plans[i]+[i+1] for i in range(len(plans))]

    print(sol(plans))

if __name__ == "__main__":
    main()  