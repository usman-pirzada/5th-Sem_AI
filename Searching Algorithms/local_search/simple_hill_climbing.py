def simple_hill_climbing(start, graph, heuristic):
    path = [start]

    while True:
        moved = False

        current = path[-1]

        for neighbor in graph[current]:
            if heuristic[neighbor] > heuristic[current]:
                path.append(neighbor)
                moved = True
                break

        # No better neighbor found
        if not moved:
            break

    return path, heuristic[current]


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}
 
# Higher value = better state
value = {
    'A': 4,
    'B': 6,
    'C': 5,
    'D': 8,
    'E': 7
}

path, final_value = simple_hill_climbing('A', graph, value)
print(f"Path: {path}\t (Final Value: {final_value})")
