from sys import stdin
from collections import defaultdict

def find_critical_links(nodes, neighbors):
    critical_links = set()
    dfs_num, dfs_low = {}, {}
    visited = set()
    dfs_time = 0

    def _dfs(node, parent=None):
        nonlocal dfs_time

        dfs_num[node] = dfs_low[node] = dfs_time
        dfs_time += 1
        visited.add(node)

        for neighbor in neighbors[node]:
            if neighbor not in visited:
                _dfs(neighbor, node)
                dfs_low[node] = min(dfs_low[node], dfs_low[neighbor])
                if dfs_num[node] < dfs_low[neighbor]:
                    critical_links.add((min(node, neighbor), max(node, neighbor)))
            elif neighbor != parent:
                dfs_low[node] = min(dfs_low[node], dfs_num[neighbor])
                
    for node in nodes:
        if node not in visited:
            _dfs(node)
    
    return critical_links

while True:
    line = stdin.readline().strip()
    if len(line) == 0:
        break
    n_nodes = int(line)
    neighbors = defaultdict(list)

    for _ in range(n_nodes):
        tokens = stdin.readline().strip().split()
        tokens[1] = tokens[1][1:-1]
        tokens = list(map(int, tokens))

        u = tokens[0]
        for v in tokens[2:]:
            neighbors[u].append(v)
        
    critical_links = list(find_critical_links(tuple(range(n_nodes)), neighbors))
    critical_links.sort()

    print(f"{len(critical_links)} critical links")
    print("".join(f"{u} - {v}\n" for u, v in critical_links))

    stdin.readline()
