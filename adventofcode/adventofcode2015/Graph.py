#!python
class Graph:
    def  __init__(self,adj,get_neighbors):
        self.adj = adj
        self.get_neighbors = get_neighbors

    def h(self,n):
        H = {s:1 for s in self.adj.keys()}
        return 1

    def astar(self,start,stop):
        open_set = set([start])
        closed_set = set()
        g = {}
        g[start] = 0
        parents = {}
        parents[start] = start

        while len(open_set) > 0:
            n = None
            for v in open_set:
                if n == None or g[v]+self.h(v) < g[n]+self.h(n):
                    n = v

            if n == None:return None

            if n == stop:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]

                path.append(start)
                path.reverse()

                return path

            for s,w in self.get_neighbors(n):
                if s not in open_set and s not in closed_set:
                    open_set.add(s)
                    parents[s] = n
                    g[s] = g[n]+w
                else:
                    if g[s] > g[n]+w:
                        g[s] = g[n]+w
                        parents[s] = n
                        if s in closed_set:
                            closed_set.remove(s)
                            open_set.add(s)

            open_set.remove(n)
            closed_set.add(n)

        return None