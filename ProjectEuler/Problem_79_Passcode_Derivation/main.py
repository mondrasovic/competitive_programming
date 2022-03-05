import collections
import sys


def topological_sort(vertices, neighbors):
    order_queue = collections.deque()
    visited = set()

    def _dfs(vertex):
        if vertex not in visited:
            visited.add(vertex)

            for neighbor in neighbors[vertex]:
                _dfs(neighbor)

            order_queue.appendleft(vertex)

    for vertex in vertices:
        _dfs(vertex)

    return order_queue


def check_login_validity(password, login):
    prev_pos = -1
    for char in login:
        curr_pos = password.index(char)
        if curr_pos <= prev_pos:
            return False
        prev_pos = curr_pos
    return True


def main():
    with open('input.txt') as in_file:
        logins = set(
            tuple(map(int, line.strip())) for line in in_file.readlines()
        )

    vertices = set()
    neighbors = collections.defaultdict(list)

    for login in logins:
        vertices = vertices | set(login)
        for first, second in zip(login[:-1], login[1:]):
            neighbors[first].append(second)

    vertices_order = topological_sort(vertices, neighbors)
    password = ''.join(map(str, vertices_order))
    print(f"Solution: {password}")


if __name__ == '__main__':
    sys.exit(main())
