#!python
import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f
    
    def __hash__(self):
        return hash(self.position)

def heuristic(current, goal):
  return abs(current[0] - goal[0]) + abs(current[1] - goal[1])    

def astar(grid, start, end):
    open_set = []
    closed_set = set()

    start_node = Node(start)
    end_node = Node(end)

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node == end_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(current_node)

        for next_pos in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + next_pos[0], current_node.position[1] + next_pos[1])

            if node_position[0] < 0 or node_position[0] >= len(grid) or \
               node_position[1] < 0 or node_position[1] >= len(grid[0]):
                continue

            if grid[node_position[0]][node_position[1]] == 1:
                continue

            neighbor = Node(node_position, current_node)

            if neighbor in closed_set:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position,end)
            neighbor.f = neighbor.g + neighbor.h

            if any(neighbor == open_node for open_node in open_set):
                continue

            heapq.heappush(open_set, neighbor)

    return None

# Example usage:
grid = [[1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1]]

start = (0, 3)
end = (6, 3)

path = astar(grid, start, end)
print(path)

