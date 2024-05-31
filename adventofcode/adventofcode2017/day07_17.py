#!python

def dict_depth(my_dict):
    if isinstance(my_dict, dict):
         
        return 1 + (max(map(dict_depth, my_dict.values()))
                                    if my_dict else 0)
         
    return 0

def get_node(program:str,lines:list[str])->dict:
    l = [line for line in lines if line.startswith(program)]
    if l:
        l=l[0]
        if "->" not in l:
            return program
        else:
            return {p:get_node(p,lines) for p in l.split(" -> ")[1].split(", ")}
    else:
        return None

def get_programs(lines:list[str])->list[str]:
    return [l.split()[0] for l in lines]

def get_unbalanced(lst:list[tuple[str,int]])->str:
    ma = max(lst,key = lambda t:t[1])
    mi = min(lst,key = lambda t:t[1])
    weights = [t[1] for t in lst]
    max_count = weights.count(ma[1])
    min_count = weights.count(mi[1])
    if len(lst) <= 1 or max_count == min_count:
        return None
    elif max_count == 1:
        return ma,ma[1]-mi[1]
    else:
        return mi,mi[1]-ma[1]  
        

def get_weight(program:str,lines:list[str])->tuple[int,int]:
    if program not in get_programs(lines):
        return -1
    else:
        l = [line for line in lines if line.startswith(program)][0]
        w = int(l.split()[1][1:-1])
        if "->" not in l:
            return w,w 
        else:
            return w,w+sum(get_weight(p,lines)[1] for p in get_node(program,lines))
        
def level(program:str,nodes:dict|str)->int:
    return program,dict_depth(nodes[program])


def sol(lines:list[str],part = 1)->str|int:
    programs = get_programs(lines)
    nodes = {p:get_node(p,lines)  for p in programs}
    levels = [level(n,nodes) for n in nodes]
    m = max(levels,key = lambda t :(t[1],t[0]))
    if part == 1:
        return m[0]
    else:
        weights=[(v,get_weight(v,lines)[1]) for v in get_node(sol(lines),lines)]
        oldweights = []
        while get_unbalanced(weights):
            oldweights = weights.copy()
            weights = [(v,get_weight(v,lines)[1]) for v in get_node(get_unbalanced(weights)[0][0],lines)]    
        
        unbal = get_unbalanced(oldweights)
        return get_weight(unbal[0][0],lines)[0]-unbal[1]
         
def main():
    with open("input07_17.txt") as inp:
        lines = [d.strip() for d in inp.readlines()]

    print(f"Part 1 : {sol(lines)}\nPart 2 : {sol(lines,2)}")

if __name__ == "__main__":
    main()