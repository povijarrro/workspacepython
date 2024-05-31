#!python
from itertools import permutations

def pathlens(data:dict[tuple[str,str],int])->list[int]:
    res=[]
    towns=set([k[0] for k in data.keys()])
    
    for p in permutations(towns) :
        dist=0
        for i in range(len(p)-1) :
            dist+=data[(p[i],p[i+1])]
        res.append(dist)
    
    return res

def sol(data:dict[tuple[str,str],int], part = 1)->int:
    pl = pathlens(data)
    return (min(pl),max(pl))[part-1]

def main() :
    with open("input09_15.txt") as inp :
        data = [d.strip() for d in inp.readlines()]
        data = [d.split(" = ") for d in data]
        data = {tuple(d[0].split(" to ")):int(d[1]) for d in data}
        data.update({d[::-1]:data[d] for d in data})

    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")

if __name__ == "__main__":
    main()
