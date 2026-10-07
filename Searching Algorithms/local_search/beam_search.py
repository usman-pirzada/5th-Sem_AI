def beam_search(start, goal, graph, heuristic, beam_width=2):
    current_beam = [([start], heuristic[start], 0)]

    while current_beam:
        for path, h_value, cost in current_beam:
            if path[-1] == goal:
                return path, cost

        candidates = []

        for path, h_value, cost in current_beam:
            current_node = path[-1]

            for neighbor, edge_cost in graph[current_node]:
                if neighbor in path:
                    continue

                new_path = path + [neighbor]
                new_cost = cost + edge_cost
                candidates.append((new_path, heuristic[neighbor], new_cost))

        if not candidates:
            break

        candidates.sort(key=lambda item: (item[1], item[2]))
        current_beam = candidates[:beam_width]

    return None, float('inf')


graph = {
    'S': [('A', 2), ('B', 4), ('C', 3), ('D', 5), ('E', 1)],
    'A': [('F', 4), ('H', 6)],
    'B': [('I', 2), ('J', 3)],
    'C': [('K', 4)],
    'D': [('L', 3), ('M', 2)],
    'E': [('N', 5)],
    'F': [('G', 3)],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'G': []
}


heuristic = {
    'S': 8,
    'A': 6,
    'B': 5,
    'C': 7,
    'D': 8,
    'E': 9,
    'F': 2,
    'H': 10,
    'I': 10,
    'J': 10,
    'K': 10,
    'L': 10,
    'M': 10,
    'N': 10,
    'G': 0
}

path, cost = beam_search('S', 'G', graph, heuristic, 2)
print(f"Goal Path: {path}\t (Path Cost: {cost})")
