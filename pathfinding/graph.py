class Graph:
    def __init__(self,graph):
        self.graph = graph
        def h(a,b):
            return 1
        self.heuristic = h

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = weight