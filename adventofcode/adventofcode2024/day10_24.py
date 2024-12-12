#!python
from itertools import product
import networkx as nx
def path(G,src,des):
    try:
        return nx.astar_path(G,src,des)
    except nx.exception.NetworkXNoPath:
        return None

def are_neighbors(a:tuple[int,int],b:tuple[int,int],diag:bool = False)->bool:
    res:bool = (abs(a[0]-b[0])<=1 and abs(b[1]-a[1])<=1 and a != b)
    return res if diag else ((a[0] == b[0] or a[1] == b[1]) and res)

def graph(tmap:list[list[int]]):
    m:int = len(tmap)
    n:int = len(tmap[0])
    edges = [(a,b) for a,b in product(list(product(range(m),range(n))),list(product(range(m),range(n)))) if are_neighbors(a,b) and (tmap[b[0]][b[1]] == tmap[a[0]][a[1]]+1)]
    return nx.from_edgelist(edges,create_using=nx.DiGraph)

def part1(tmap:list[list[int]])->int:
    G = graph(tmap)
    return len([(a,b) for a,b in product(G.nodes(),G.nodes()) if tmap[a[0]][a[1]] == 0 and tmap[b[0]][b[1]] == 9 and path(G,a,b)])

def part2(tmap:list[list[int]])->int:
    G = graph(tmap)
    gn = G.nodes()
    return sum([len(list(nx.all_shortest_paths(G,a,b))) for a,b in product(gn,gn) if tmap[a[0]][a[1]] == 0 and tmap[b[0]][b[1]] == 9 and path(G,a,b)])


def main()->None:
    with open("./input10_24.txt") as inp:
        tmap:list[list[int]] = [list(map(int,list(d))) for d in inp.read().strip().split("\n")]

    with open("./example10_24.txt") as inp:
        extmap:list[list[int]] = [list(map(int,list(d))) for d in inp.read().strip().split("\n")]

    print(f"Part 1 : {part1(tmap)}\nPart 2 : {part2(tmap)}")
if __name__ == "__main__":
    main()    