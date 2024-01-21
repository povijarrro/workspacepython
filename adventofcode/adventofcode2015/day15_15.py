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

def total(property:str,weights:tuple[int], data:dict[str,dict[str,int]])->int:
    tot = 0
    props = [v[property] for v in data.values()]
    
    for i,w in enumerate(weights) :
        tot += w*props[i]
        
    return tot

def score(weights:tuple[int], data:dict[str,dict[str,int]])->int:
    tots = []
    for prop in list(data.values())[0].keys():
        m = max(total(prop,weights,data),0)
        tots.append(m)

    return reduce(lambda x, y : x*y,tots)

def optimal_score(data:dict[str,dict[str,int]])->int:
    optim = 0
    for var in variations(len(data.keys()),100):
        if score(var,data)>optim:
            optim = var

    return optim

if __name__ == "__main__":
    with open("example15_15.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
        data = [d+"," for d in data]
        data = [d.split() for d in data]
        data = {spl[0][:-1]:{spl[i]:int(spl[i+1][:-1]) for i in range(1,8,2)} for spl in data}

    print(optimal_score(data))