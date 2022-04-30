import sys


def read_line():
    return sys.stdin.readline().strip()


def is_bicolorable(nodes, graph):
    no_color, color_1, color_2 = 0, 1, 2
    colors = {node: no_color for node in nodes}

    def _dfs(node, prev_color=no_color):
        curr_color = colors[node]
        if curr_color != no_color:
            return prev_color != curr_color

        curr_color = color_2 if prev_color == color_1 else color_1
        colors[node] = curr_color

        for neighbor in graph.get(node, []):
            if not _dfs(neighbor, curr_color):
                return False

        return True

    return all(_dfs(node) for node in nodes)


def add_edge(graph, src_node, dst_node):
    neighbors = graph.get(src_node)
    if neighbors is None:
        neighbors = []
        graph[src_node] = neighbors
    neighbors.append(dst_node)


def main():
    while True:
        n_nodes = int(read_line())
        if n_nodes == 0:
            return 0

        graph = {}
        nodes = list(range(n_nodes))
        n_edges = int(read_line())

        for _ in range(n_edges):
            src_node, dst_node = map(int, read_line().split())
            add_edge(graph, src_node, dst_node)
            add_edge(graph, dst_node, src_node)

        state = "" if is_bicolorable(nodes, graph) else "NOT "
        print(f"{state}BICOLORABLE.")


if __name__ == '__main__':
    sys.exit(main())
