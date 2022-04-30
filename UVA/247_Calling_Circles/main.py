import collections
import itertools
import operator
import sys


def read_line():
    return sys.stdin.readline().strip()


def find_scc_kosaraju(nodes, neighbors):
    neighbors_inv = collections.defaultdict(set)
    visited = set()
    dfs_order_nodes_stack = []

    for root_node in nodes:
        if root_node in visited:
            continue

        stack = [root_node]
        visited.add(root_node)

        while stack:
            curr_node = stack[-1]

            for neighbor in neighbors[curr_node]:
                neighbors_inv[neighbor].add(curr_node)

                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    break
            else:
                stack.pop()
                dfs_order_nodes_stack.append(curr_node)

    components = {node: None for node in nodes}

    while dfs_order_nodes_stack:
        root_node = dfs_order_nodes_stack.pop()
        if components[root_node] is not None:
            continue

        stack = [root_node]
        components[root_node] = root_node

        while stack:
            curr_node = stack[-1]

            for neighbor in neighbors_inv[curr_node]:
                if components[neighbor] is None:
                    components[neighbor] = root_node
                    stack.append(neighbor)
                    break
            else:
                stack.pop()

    return components


def find_calling_circles(names, call_contacts):
    components = find_scc_kosaraju(names, call_contacts)
    component_getter = operator.itemgetter(1)
    components = sorted(components.items(), key=component_getter)

    for _, calling_circle in itertools.groupby(components, component_getter):
        yield (name for name, _ in calling_circle)


def main():
    sep = ""

    for data_set_n in itertools.count(1):
        n_people, n_calls = map(int, read_line().split())
        if (n_people == 0) and (n_calls == 0):
            return 0

        names = set()
        call_contacts = collections.defaultdict(set)
        for _ in range(n_calls):
            caller, callee = read_line().split()
            names.add(caller)
            names.add(callee)
            call_contacts[caller].add(callee)

        print(f"{sep}Calling circles for data set {data_set_n}:")
        for calling_circle in find_calling_circles(names, call_contacts):
            print(", ".join(calling_circle))
        sep = "\n"


if __name__ == '__main__':
    sys.exit(main())
