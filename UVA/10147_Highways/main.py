def dist(u, v):
    return (u[0] - v[0]) ** 2 + (u[1] - v[1]) ** 2

class DisjointSet:
    def __init__(self, n_nodes) -> None:
        self.parent = list(range(n_nodes))
        self.size = [1] * n_nodes
    
    def union(self, u, v):
        p_u, p_v = self.find(u), self.find(v)
        if p_u != p_v:
            if self.size[p_u] > self.size[p_v]:
                p_u, p_v = p_v, p_u
            self.parent[p_u] = p_v
            self.size[p_v] += self.size[p_u]

    def find(self, u):
        p = self.parent[u]
        if p != u:
            p = self.find(p)
            self.parent[u] = p
        return p

n_cases = int(input())
sep = ""

for _ in range(n_cases):
    print(sep, end="")
    sep = "\n"

    input()
    n_towns, town_positions = int(input()), []
    for _ in range(n_towns):
        xy_pos = tuple(map(int, input().split()))
        town_positions.append(xy_pos)
    ds = DisjointSet(n_towns)
    n_highways = int(input())
    for _ in range(n_highways):
        u, v = tuple(map(int, input().split()))
        ds.union(u - 1, v - 1)

    edges = []
    for u in range(n_towns - 1):
        for v in range(u + 1, n_towns):
            if ds.find(u) != ds.find(v):
                cost = dist(town_positions[u], town_positions[v])
                edges.append((cost, u, v))
    
    n_edges_added = 0
    for edge in sorted(edges):
        if n_edges_added == n_towns - 1:
            break
        _, u, v = edge
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            n_edges_added += 1
            print(f"{u + 1} {v + 1}")
    
    if n_edges_added == 0:
        print("No new highways need")
