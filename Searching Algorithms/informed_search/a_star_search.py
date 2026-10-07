def a_star_search(start, goal, graph, heuristic):
    g_cost = {start: 0}
    f_cost = heuristic[start] + g_cost[start]

    open_list = [(start, f_cost)]

    came_from = {start: None}

    close_list = set()

    while open_list:
        open_list.sort(key=lambda item: (item[1]))

        current_node, current_f = open_list.pop(0)

        if current_node in close_list:
            continue

        close_list.add(current_node)

        if current_node == goal:
            path = []

            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]

            path.reverse()
            return path, g_cost[goal]

        for neighbor, edge_cost in graph[current_node].items():
            new_g = g_cost[current_node] + edge_cost
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                came_from[neighbor] = current_node

                new_f = heuristic[neighbor] + new_g
                open_list.append((neighbor, new_f))

    return None, float('inf')


graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {}
}

heuristic = {
    'A': 14,
    'B': 12,
    'C': 11,
    'D': 6,
    'E': 4,
    'F': 11,
    'G': 0
}

path, cost = a_star_search('A', 'G', graph, heuristic)
print(f"Goal Path: {path}\t (Path Cost: {cost})")
