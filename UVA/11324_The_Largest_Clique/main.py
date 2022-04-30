import sys
import collections


def read_line():
    return sys.stdin.readline().strip()


def add_edge(graph, src_node, dst_node):
    neighbors = graph.get(src_node)

    if neighbors is None:
        neighbors = []
        graph[src_node] = neighbors

    neighbors.append(dst_node)


def build_graph(n_nodes, src_links, dst_links):
    nodes = list(range(1, n_nodes + 1))
    graph_neighbors = {}

    for src_node, dst_node in set(zip(src_links, dst_links)):
        add_edge(graph_neighbors, src_node, dst_node)

    return nodes, graph_neighbors


def graph_find_scc(nodes, graph_neighbors):
    graph_inv_neighbors = {node: set() for node in nodes}
    dfs_nodes = []
    visited = set()

    for root in nodes:
        if root in visited:
            continue

        visited.add(root)
        stack = [root]

        while stack:
            src_node = stack[-1]

            for dst_node in graph_neighbors.get(src_node, []):
                graph_inv_neighbors[dst_node].add(src_node)

                if dst_node not in visited:
                    visited.add(dst_node)
                    stack.append(dst_node)
                    break
            else:
                stack.pop()
                dfs_nodes.append(src_node)

    components = {node: None for node in nodes}

    while dfs_nodes:
        root = dfs_nodes.pop()

        if components[root] is not None:
            continue

        components[root] = root
        stack = [root]

        while stack:
            src_node = stack[-1]
            for dst_node in graph_inv_neighbors[src_node]:
                if components[dst_node] is None:
                    components[dst_node] = root
                    stack.append(dst_node)
                    break
            else:
                stack.pop()

    return components


def calc_component_sizes(components):
    return collections.Counter(components.values())


def topological_sort_condensed(nodes, graph_neighbors):
    components = graph_find_scc(nodes, graph_neighbors)

    condensed_graph_neighbors = {}
    condensed_nodes = set()

    for src_node, neighbors in graph_neighbors.items():
        src_component = components[src_node]
        condensed_nodes.add(src_component)

        for dst_node in neighbors:
            dst_component = components[dst_node]

            if src_component != dst_component:
                condensed_nodes.add(dst_component)
                add_edge(
                    condensed_graph_neighbors, src_component, dst_component
                )

    visited = set()
    nodes_sorted = []

    for root in condensed_nodes:
        if root in visited:
            continue

        stack = [root]
        visited.add(root)

        while stack:
            src_node = stack[-1]
            for dst_node in condensed_graph_neighbors.get(src_node, []):
                if dst_node not in visited:
                    visited.add(dst_node)
                    stack.append(dst_node)
                    break
            else:
                stack.pop()
                nodes_sorted.append(src_node)

    component_sizes = calc_component_sizes(components)

    return nodes_sorted, condensed_graph_neighbors, component_sizes


def find_longest_path(nodes, graph_neighbors, component_sizes):
    max_paths = {node: component_sizes[node] for node in nodes}
    longest_path = 0

    for node in nodes:
        sub_max_path = 0

        for neighbor in graph_neighbors.get(node, []):
            sub_max_path = max(sub_max_path, max_paths[neighbor])

        max_paths[node] += sub_max_path
        longest_path = max(longest_path, max_paths[node])

    return longest_path


def main():
    n_cases = int(read_line())

    for _ in range(n_cases):
        n_nodes, n_edges = map(int, read_line().split())
        nodes = range(1, n_nodes + 1)
        neighbors = {}

        for _ in range(n_edges):
            src_node, dst_node = map(int, read_line().split())
            if src_node not in neighbors:
                neighbors[src_node] = []
            neighbors[src_node].append(dst_node)

        if (n_nodes == 0) and (n_edges == 0):
            print("0")
            continue

        if (n_nodes > 0) and (n_edges == 0):
            print("1")
            continue

        nodes_sorted, condensed_graph_neighbors, component_sizes = topological_sort_condensed(
            nodes, neighbors
        )
        print(
            find_longest_path(
                nodes_sorted, condensed_graph_neighbors, component_sizes
            )
        )

    return 0


if __name__ == '__main__':
    sys.exit(main())
