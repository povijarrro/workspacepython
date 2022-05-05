#!python
from collections import defaultdict
import sys

def neighbours(i,j,m,n):
    res = []
    
    if i in range(m) and i-1 in range(m) and j in range(n):
        res.append((i-1,j))
    if i in range(m) and i+1 in range(m) and j in range(n):
        res.append((i+1,j))
    if i in range(m) and j-1 in range(n) and j in range(n):
        res.append((i, j-1))
    if i in range(m) and j+1 in range(n) and j in range(n):
        res.append((i,j+1))
    
    return res

def get_risk(data):
    m = len(data)
    n = len(data[0]) if m>0 else 0
    risks = []
    low_points=[]
    for i in range(m):
        for j in range(n):
            is_risky = True
            for pos in neighbours(i,j,m,n):
                if data[i][j]>=data[pos[0]][pos[1]]:
                    is_risky = False
            
            if is_risky:
                risks.append(data[i][j]+1)
                low_points.append((i,j))
            

    
    return low_points, sum(risks)

def generate_graph(data):
    dd=defaultdict(set)
    m = len(data)
    n = len(data[0]) if m>0 else 0
    for i in range(m):
        for j in range(n):
            for neighbour in neighbours(i,j,m,n):
                if data[neighbour[0]][neighbour[1]]!= 9 and data[i][j] != 9:
                    dd[(i,j)].add(neighbour)
    return dd


def dfs(graph,start,visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def get_basins(data):
    res = []
    for low_point in get_risk(data)[0]:
        res.append(dfs(generate_graph(data),low_point))

    return res

data = sys.argv[1:]
data = [[int(x[i]) for i in range(len(x))] for x in data]
print(get_risk(data)[1])
print(sorted([len(x) for x in get_basins(data)]))
