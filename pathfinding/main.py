#!python
from astar import a_star
from graph import Graph 
from collections import deque


def main():
    g : Graph = Graph({"A":("B","C"),
                       "B":("A","D"),
                       "C":("A","D"),
                       "D":("B","C"),
                       "E":("D",)})
    
    start = "A"
    end = "E" 
    
    came_from,_ = a_star(g,start,end)
    print(came_from)
    
    path = deque([])
    current = end
    while current != start:
        path.appendleft(current)
        current = came_from[current] 
    path.appendleft(start)      
    
    print(path)


if __name__ == "__main__":
    main()
