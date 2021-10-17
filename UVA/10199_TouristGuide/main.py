from sys import stdin
from collections import defaultdict

def find_articulations(nodes, neighbors):
    visited, dfn, low, articulations = set(), {}, {}, set()
    time = 0

    def _dfs(node, parent=None):
        nonlocal time

        visited.add(node)
        n_children = 0
        dfn[node] = low[node] = time
        time += 1

        for neighbor in neighbors[node]:
            if neighbor == parent:
                continue

            if neighbor in visited:
                low[node] = min(low[node], dfn[neighbor])
            else:
                _dfs(neighbor, node)
                low[node] = min(low[node], low[neighbor])
                if parent and (low[neighbor] >= dfn[node]):
                    articulations.add(node)
                n_children += 1
        
        if (not parent) and (n_children > 1):
            articulations.add(node)
    
    for node in nodes:
        if node not in visited:
            _dfs(node)
    
    return articulations

case_id, sep = 1, ""
n_nodes = int(input())

while n_nodes > 0:
    nodes = [stdin.readline().strip() for _ in range(n_nodes)]
    n_edges = int(input())
    neighbors = defaultdict(list)
    
    for _ in range(n_edges):
        src, dst = stdin.readline().split()
        neighbors[src].append(dst)
        neighbors[dst].append(src)
    
    articulations = find_articulations(nodes, neighbors)

    print(f"{sep}City map #{case_id}: {len(articulations)} camera(s) found")
    if len(articulations):
        print("\n".join(sorted(list(articulations))))

    case_id += 1
    sep = "\n"
    n_nodes = int(input())
