#!python
import networkx as nx
def main():
    with open("input24_04.txt") as inp:
        data:list[str] = [d.strip() for d in inp.readlines()]
        edges = [(d.split(" <-> ")[0],d.split(" <-> ")[1]) for d in data]
    
    g:nx.Graph = nx.from_edgelist(edges)
    g = g.to_undirected()
    sol1 = len(set([d.split(" <-> ")[0] for d in data]+[d.split(" <-> ")[1] for d in data]))
    sol2 = len([v for v in g.nodes() if len(nx.astar_path(g,"STT", v))<=4])
    sol3 = sum([len(nx.astar_path(g,"STT", v))-1 for v in g.nodes()])

    print(f"Part 1 : {sol1}\nPart 2 : {sol2}\nPart 3 : {sol3}")
if __name__ == "__main__" :
    main() 