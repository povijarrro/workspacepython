#!python
from functools import reduce
from itertools import product

def appended(lst:list,item)->list:
    lst.append(item)
    return lst

def variations(l:int,s:int)->list[tuple]:
    if l == 1 : return (s,)
    if l == 2 : return [(i,s-i) for i in range(s+1)]
    kwargs=(l-1)*[range(s+1)]
    prod = list(product(*kwargs))
    return [tuple(appended(list(p),s-sum(p))) for p in prod if sum(p)<=s]

def total(prop:str,weights:tuple[int], data:dict[str,dict[str,int]])->int:
    tot = 0
    props = [v[prop] for v in data.values()]
    
    for i,w in enumerate(weights) :
        tot += w*props[i]
        
    return tot

def score(weights:tuple[int], data:dict[str,dict[str,int]])->int:
    tots = []
    for prop in list(data.values())[0].keys():
        if prop == "calories" :
            break
        m = max(total(prop,weights,data),0)
        tots.append(m)

    return reduce(lambda x, y : x*y,tots)

def optimal_score(data:dict[str,dict[str,int]], cals = 0)->int:
    optim = 0
    for var in variations(len(data.keys()),100):
        sc = score(var,data) 
        if sc>optim :
            if cals == 0 : optim = sc
            elif total("calories",var,data) == cals :
                optim = sc

    return optim

def sol(data:dict[str,dict[str,int]], part = 1)->int:
    return optimal_score(data,500*(part-1))

def main():
    with open("input15_15.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
        data = [d+"," for d in data]
        data = [d.split() for d in data]
        data = {spl[0][:-1]:{spl[i]:int(spl[i+1][:-1]) for i in range(1,10,2)} for spl in data}

    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")

if __name__ == "__main__":
    main()    