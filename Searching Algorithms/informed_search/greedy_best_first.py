def greedy_best_first(start, goal, graph, heuristic):
    frontier = [(start, heuristic[start])]

    came_from = {start: None}

    visited = set()

    while frontier:
        frontier.sort(key=lambda item: item[1])

        current_node, current_h = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []

            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]

            path.reverse()
            return path

        for neighbor in graph[current_node]:
            if neighbor in visited:
                continue

            came_from[neighbor] = current_node
            frontier.append((neighbor, heuristic[neighbor]))

    return None


graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 7,
    'F': 3,
    'G': 6,
    'H': 2,
    'I': 0
}

goal_path = greedy_best_first('A', 'I', graph, heuristic)
print("Goal Path:", goal_path)
