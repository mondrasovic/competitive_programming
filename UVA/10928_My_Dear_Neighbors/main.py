import collections
import sys


def read_line():
    return sys.stdin.readline().strip()


n_cases = int(read_line())

for _ in range(n_cases):
    neighbors = collections.defaultdict(list)
    n_places = int(read_line())
    for src_place in range(1, n_places + 1):
        for neighbor_place in map(int, read_line().split()):
            neighbors[src_place].append(neighbor_place)

    min_neighbors_count = sys.maxsize
    min_neighbors_places = None

    for place, curr_neighbors in neighbors.items():
        curr_neighbors_count = len(curr_neighbors)
        if curr_neighbors_count < min_neighbors_count:
            min_neighbors_count = curr_neighbors_count
            min_neighbors_places = [place]
        elif curr_neighbors_count == min_neighbors_count:
            min_neighbors_places.append(place)

    print(" ".join(map(str, sorted(min_neighbors_places))))

    read_line()
