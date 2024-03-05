#!python
from itertools import combinations

def sol(mat,part=1):
    if part == 1 :
        return sum(r[-1]-r[0] for r in mat)
    else : 
        res=0
        for r in mat:
            for c in combinations(r,2):
                if c[1]%c[0] == 0:
                    res += c[1]//c[0]
                    break
        return res

if __name__ == "__main__":
    with open("input02_17.txt") as inp:
        spreadsheet = [sorted(list(map(int,d.strip().split()))) for d in inp.readlines()] 

    print(f"Part 1 : {sol(spreadsheet)}\nPart 2 : {sol(spreadsheet,2)}")  