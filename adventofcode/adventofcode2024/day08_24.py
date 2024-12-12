#!python
from itertools import combinations, product
def line(a:tuple[int,int],b:tuple[int,int]):
    return lambda t: (a[0]+t*(b[0]-a[0]),a[1]+t*(b[1]-a[1]))

def is_valid(a:tuple,dim)->bool:
    return a[0] in range(dim[0]) and a[1] in range(dim[1])

def antinodes(a:tuple[int,int],b:tuple[int,int], dim:tuple[int,int],p2:bool=False)->list[tuple[int,int]]:
    if not p2:
        c:tuple[int,int] = line(a,b)(2)
        d:tuple[int] = line(a,b)(-1)
        res:list[tuple[int,int]] = []
        if is_valid(c,dim):
            res.append(c)
        if is_valid(d,dim):
            res.append(d)
        return res
    else:
         return [line(a,b)(t) for t in range(-max(dim),max(dim)) if is_valid(line(a,b)(t),dim)]        

def sol(data:list[str],p2)->int:
    m:int = len(data)
    n:int = len(data[0])
    anti = [[False for _ in range(n)] for _ in range(m)]
    prod = list(product(range(m),range(n)))
    comprod = combinations(prod,2)
    for a,b in comprod:
        if (data[a[0]][a[1]] == data[b[0]][b[1]]) and (data[a[0]][a[1]] != "."):
            for i,j in antinodes(a,b,(m,n),p2):
                anti[i][j] = True
             
    return sum(sum(an) for an in anti)

def part1(data:list[str])->int:
    return sol(data,False)

def part2(data:list[str])->int:
    return sol(data,True)

def main()-> None:
    with open("./input08_24.txt") as inp:
        data = inp.read().strip().split("\n")

    with open("./example08_24.txt") as inp:
        exdata = inp.read().strip().split("\n")
      
    print(f"Part 1 : {part1(data)}\nPart 2 : {part2(data)}")
if __name__ == "__main__":
    main()    