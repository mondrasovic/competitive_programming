import dataclasses
import itertools
import math
import sys


@dataclasses.dataclass(frozen=True)
class Edge:
    src_node: int
    dst_node: int
    cost: float


class DisjointSet:
    def __init__(self, items) -> None:
        self.parents = {item: item for item in items}
        self.sizes = {item: 1 for item in items}

    def union(self, item_1, item_2):
        parent_1 = self.find(item_1)
        parent_2 = self.find(item_2)

        if parent_1 != parent_2:
            size_1 = self.sizes[parent_1]
            size_2 = self.sizes[parent_2]

            if size_1 <= size_2:
                self.parents[parent_1] = parent_2
                self.sizes[parent_2] += size_1
            else:
                self.parents[parent_2] = parent_1
                self.sizes[parent_1] += size_2

    def find(self, item):
        parent = self.parents[item]

        if parent != item:
            parent = self.find(parent)
            self.parents[item] = parent

        return parent


def read_line():
    return sys.stdin.readline().strip()


def min_spanning_tree_cost(nodes, edges):
    nodes_disjoint_set = DisjointSet(nodes)

    tree_cost = 0
    used_edges = 0
    edges.sort(key=lambda e: (e.cost, e.src_node, e.dst_node))

    for edge in edges:
        if used_edges == len(nodes):
            break

        src_component = nodes_disjoint_set.find(edge.src_node)
        dst_component = nodes_disjoint_set.find(edge.dst_node)

        if src_component != dst_component:
            nodes_disjoint_set.union(edge.src_node, edge.dst_node)
            tree_cost += edge.cost
            used_edges += 1

    return tree_cost


def main():
    n_cases = int(read_line())
    case_sep = ""

    for _ in range(n_cases):
        read_line()

        n_nodes = int(read_line())
        nodes = list(range(n_nodes))
        node_positions = [
            tuple(map(float,
                      read_line().split())) for _ in range(n_nodes)
        ]

        edges = []
        for src_node, dst_node in itertools.combinations(nodes, r=2):
            src_x, src_y = node_positions[src_node]
            dst_x, dst_y = node_positions[dst_node]
            node_dist = math.sqrt((dst_x - src_x)**2 + (dst_y - src_y)**2)
            edges.append(Edge(src_node, dst_node, node_dist))

        print(f"{case_sep}{min_spanning_tree_cost(nodes, edges):.2f}")
        case_sep = "\n"

    return 0


if __name__ == '__main__':
    sys.exit(main())
