#!python
from astar import a_star, reconstruct_path
from graph import Graph 
def main():
    graph = Graph({})
    graph.add_edge('A', 'B', 1)
    graph.add_edge('B', 'A', 1)
    graph.add_edge('A', 'C', 1)
    graph.add_edge('C', 'A', 1)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('D', 'B', 1)
    graph.add_edge('C', 'D', 1)
    graph.add_edge('D', 'C', 1)
    graph.add_edge('D', 'E', 1)
    graph.add_edge('E', 'D', 1)

    print(graph.graph)
    start_node = 'A'
    goal_node = 'E'
    costs,path = a_star(graph, start_node, goal_node)
    print(path)
    print(costs)



if __name__ == "__main__":
    main()