import heapq

def a_star(graph, start, goal):
    queue = []
    heapq.heappush(queue, (0, start))
    costs = {start: 0}
    path = {start: None}

    while queue:
        (cost, current) = heapq.heappop(queue)

        if current == goal:
            break

        for neighbor in graph.graph[current]:
            new_cost = costs[current] + graph.graph[current][neighbor]

            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                priority = new_cost + graph.heuristic(goal, neighbor)
                heapq.heappush(queue, (priority, neighbor))
                path[neighbor] = current

    return costs, reconstruct_path(path,start,goal)

def reconstruct_path(path, start, goal):
    current = goal
    path_to_goal = []

    while current != start:
        path_to_goal.append(current)
        current = path[current]

    path_to_goal.append(start)  # add the start node
    path_to_goal.reverse()  # reverse the list to get the path from start to goal

    return path_to_goal