def steepest_ascent_hill_climbing(start, graph, value):
    path = [start]

    while True:
        current = path[-1]

        if not graph[current]:
            break

        best_neighbor = max(graph[current], key=lambda node: value[node])

        if value[best_neighbor] > value[current]:
            path.append(best_neighbor)
        else:
            break

    return path, value[current]


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

path, final_value = steepest_ascent_hill_climbing('A', graph, value)
print(f"Path: {path}\t (Final Value: {final_value})")
