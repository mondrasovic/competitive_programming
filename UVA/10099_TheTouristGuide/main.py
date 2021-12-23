from sys import stdin
from math import ceil
from collections import defaultdict
from heapq import heappush, heappop

def read_ints():
    return tuple(map(int, stdin.readline().strip().split()))

def find_max_min_path_cost(neighbors, start, end):
    pq = [(-10 ** 9, start)]
    visited = set([start])

    while len(pq) > 0:
        max_min_cost, node = heappop(pq)
        if node == end:
            return -max_min_cost
        visited.add(node)
        for neighbor, cost in neighbors[node]:
            if neighbor not in visited:
                heappush(pq, (-min(-max_min_cost, cost), neighbor))
    
    return None


scenario = 1
while True:
    n_nodes, n_edges = read_ints()
    if n_nodes == 0:
        break

    neighbors = defaultdict(list)
    for _ in range(n_edges):
        src, dst, cost = read_ints()
        neighbors[src].append((dst, cost))
        neighbors[dst].append((src, cost))

    start, end, n_tourists = read_ints()
    max_min_cost = find_max_min_path_cost(neighbors, start, end)
    n_trips = int(ceil(n_tourists / (max_min_cost - 1)))
    print(f"Scenario #{scenario}\nMinimum Number of Trips = {n_trips}\n")

    scenario += 1
