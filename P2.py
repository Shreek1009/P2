def astarAlgo(start_node, stop_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while len(open_set) != 0:
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v
        if n == stop_node or n not in graph_nodes:
            pass
        else:
            for (neighbor, weight) in get_neighbours(n):
                if neighbor not in open_set and neighbor not in closed_set:
                    open_set.add(neighbor)
                    parents[neighbor] = n
                    g[neighbor] = g[n] + weight
                else:
                    if g.get(neighbor, float('inf')) > g[n] + weight:
                        g[neighbor] = g[n] + weight
                        parents[neighbor] = n
                        if neighbor in closed_set:
                            closed_set.remove(neighbor)
                            open_set.add(neighbor)
        if n is None:
            print("Path Doesn't exist!")
            return None
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print('Path Found:', path)
            return path
        open_set.remove(n)
        closed_set.add(n)
    print("Path Doesn't Exist")
    return None

def get_neighbours(v):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return []

def heuristic(n):
    H_dist = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 4,
        'I': 1,
        'J': 0
    }
    return H_dist[n]

graph_nodes = {
    'A': [('B', 5), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)]
}

astarAlgo('A', 'J')
