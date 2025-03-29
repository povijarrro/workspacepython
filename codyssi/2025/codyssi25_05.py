#!python
def manhattan(t1,t2):
    return abs(t1[0]-t2[0])+abs(t1[1]-t2[1])

def closest(islands, start = (0,0)):
    
    sor = sorted(set(islands)-set([start]), key = lambda x: manhattan(start,x))
    msor = [manhattan(start,t) for t in sor]
    sor = [t for t in sor if manhattan(start,t) == msor[0]]
    return sorted(sor)[0]

def travel(islands,start = (0,0)):
    path = []
    path_len = 0
    curmap:list[tuple[int,int]] = islands[:]
    clos = start
    while curmap:
        oldclos = clos
        clos = closest(curmap, clos)
        path_len += manhattan(oldclos,clos)
        path.append(clos)
        curmap.remove(clos)
    return path, path_len

def main():
    with open("input25_05.txt") as inp:
        data  = [d.strip() for d in inp.readlines()]
        islands = [eval(d) for d in data]
    
    sol1 = max(manhattan((0,0),t) for t in islands)-min(manhattan((0,0),t) for t in islands)
    clos = closest(islands,(0,0))
    clos2clos = closest(islands,clos)
    sol2 = manhattan(clos,clos2clos)
    sol3 = travel(islands,(0,0))[1]
    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")

if __name__ == "__main__" :
    main() 