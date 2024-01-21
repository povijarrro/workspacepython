#!python

from itertools import permutations


def neighbours(person:str,lst:list[str])->tuple[str,str]:
    i = lst.index(person)
    return lst[i-1],lst[(i+1)%len(lst)]

def happiness(person:str, lst:list[str],data:dict[tuple[str,str],int])->int:
    nbs = neighbours(person,lst)
    return data[(person,nbs[0])]+data[(person,nbs[1])] 

def total_happiness(lst:list[str],data:dict[tuple[str,str],int])->int:
    return sum(happiness(person,lst,data) for person in lst)

def max_happ(data:dict[tuple[str,str],int])->int:
    hpns=[]
    people = list(set([k[0] for k in data.keys()]))
    
    for p in permutations(people):
        hpns.append(total_happiness(p,data))

    return max(hpns)
def sol(data:dict[tuple[str,str],int],part = 1)->int:
    if part == 1 : return max_happ(data)
    
    with_me = {}
    for k,v in data.items():
        with_me[k]=v
        with_me[("povijarrro",k[0])]=0
        with_me[(k[0],"povijarrro")]=0
        
    return max_happ(with_me)


if __name__ == "__main__" :
    with open("input13_15.txt") as inp :
        data = [d.strip() for d in inp.readlines()]
        data = [d.replace(" would gain "," ") for d in data]
        data = [d.replace(" would lose "," -") for d in data]
        data = [d.replace(" happiness units by sitting next to "," ") for d in data]
        data = [d.split() for d in data]
        data = {(spl[0],spl[2][:-1]):int(spl[1]) for spl  in data}
    

    print(f"Part 1 : {sol(data)}\nPart 2 : {sol(data,2)}")
