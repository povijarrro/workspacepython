#!python
 
from itertools import chain, combinations



def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def minlen(lst:list):
    return min(len(i) for i in lst)

def get_filled(amount:int,capacities:list[int],minimal = False)->list[tuple]:
    filled = []
    
    idxs =set(range(len(capacities)))
    for ps in powerset(idxs):
        if sum(capacities[i] for i in ps) == amount:filled.append(ps)

    ml = minlen(filled)
    return filled if not minimal else [f for f in filled if len(f) == ml] 

def sol(amount:int,capacities:list[int],part = 1)->int:
    return len(get_filled(amount,capacities,part != 1))

def main():
    with open("input17_15.txt") as inp:
        capacities = sorted([int(d.strip()) for d in inp.readlines()])

    filled=get_filled(150,capacities)  
    ml= minlen(filled)
    print(f"Part 1 : {sol(150,capacities)}\nPart 2 : {sol(150,capacities,2)}") 

if __name__ == "__main__":
    main()