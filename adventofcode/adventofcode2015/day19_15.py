#!python
from Graph import Graph


def get_molecules(data:dict[str,list[str]],molecule:str):

    for k,v in data:
        for i in range(len(molecule)-len(k)+1):
            if molecule[i:i+len(k)] == k :
                yield molecule[:i]+v+molecule[i+len(k):]
          

def sol(data:dict[str,list[str]],molecule:str,part=1)->int:
    pairs = [(k,v) for k in data for v in data[k]]
    if part == 1 : return len(set(get_molecules(pairs,molecule)))
    else:
        d = {k:[(s,1) for s in v] for k,v in data.items()}
        graph = Graph(d,lambda v :[(s,1) for s in set(get_molecules(pairs,v))])
        path = graph.astar("e",molecule)
        print(path)
        return len(path)-1

if __name__ == "__main__":
    with open("input19_15.txt") as inp:
        data = [d.strip() for d in inp.readlines()]
        molecule = data[-1]
        data = [d.split(" => ") for d in data[:-2]]
        data2={d[0]:[] for d in data}
        i=0
        while i in range(len(data)-1):
            
            data2[data[i][0]].append(data[i][1])
            if data[i][0]==data[i+1][0]:
                data2[data[i][0]].append(data[i+1][1])
                i+=1
            i+=1    
        data2[data[i][0]].append(data[i][1])    
        data=data2
    
    adj = {(0,0):[((0,1),1),((1,0),1)],
            (0,1):[((0,0),1),((0,2),1)],
            (0,2):[((0,1),1)],
            (1,0):[((0,0),1),((2,0),1)],
            (2,0):[((1,0),1),((2,1),1)],
            (2,1):[((2,0),1),((2,2),1)],
            (2,2):[((2,1),1)]}
    
    graph = Graph(adj,lambda v:adj[v])
    
    print(graph.astar((0,2),(2,2)))
    print(sol(data,molecule,2))
    
