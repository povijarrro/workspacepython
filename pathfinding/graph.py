class Graph:
    
    def __init__(self,neighs:dict[str,tuple[str]]):
        self.neighs = neighs
    
    def neighbors(self,node:str)->tuple[str]:
        return self.neighs[node] if node in self.neighs else tuple()
    
    def cost(self,start:str,goal:str)->int:
        return 1



