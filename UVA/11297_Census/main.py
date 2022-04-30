import functools
import sys


class Node:
    _INF = sys.maxsize

    def __init__(self, vals_grid, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        self.min_val = None
        self.max_val = None

        self.top_left = None
        self.top_right = None
        self.bottom_right = None
        self.bottom_left = None

        self._init_node(vals_grid)

    def query_range_min_max(self, x1, y1, x2, y2):
        if (self.x1, self.y1, self.x2, self.y2) == (x1, y1, x2, y2):
            return (self.min_val, self.max_val)

        min_val, max_val = self._INF, -self._INF
        for node in self._iter_existing_nodes():
            valid, overlap = self._calc_overlap_region_if_valid(
                node, x1, y1, x2, y2
            )
            if valid:
                curr_min_val, curr_max_val = node.query_range_min_max(*overlap)
                min_val = min(min_val, curr_min_val)
                max_val = max(max_val, curr_max_val)

        return (min_val, max_val)

    def update_val(self, x, y, val):
        if (self.x1, self.y1, self.x2, self.y2) == (x, y, x, y):
            self.min_val = self.max_val = val
        else:
            self.min_val, self.max_val = self._INF, -self._INF

            for node in self._iter_existing_nodes():
                if (node.x1 <= x <= node.x2) and (node.y1 <= y <= node.y2):
                    node.update_val(x, y, val)

                self.min_val = min(self.min_val, node.min_val)
                self.max_val = max(self.max_val, node.max_val)

    def _init_node(self, vals_grid):
        if (self.x1 == self.x2) and (self.y1 == self.y2):
            self.min_val = self.max_val = vals_grid[self.x1][self.y1]
        else:
            mid_x = (self.x1 + self.x2) // 2
            mid_y = (self.y1 + self.y2) // 2

            _c = functools.partial(self._create_subnode_if_exists, vals_grid)
            self.top_left = _c(self.x1, self.y1, mid_x, mid_y)
            self.top_right = _c(mid_x + 1, self.y1, self.x2, mid_y)
            self.bottom_right = _c(mid_x + 1, mid_y + 1, self.x2, self.y2)
            self.bottom_left = _c(self.x1, mid_y + 1, mid_x, self.y2)

            self.min_val, self.max_val = self._INF, -self._INF
            for node in self._iter_existing_nodes():
                self.min_val = min(self.min_val, node.min_val)
                self.max_val = max(self.max_val, node.max_val)

    def _create_subnode_if_exists(self, vals_grid, x1, y1, x2, y2):
        if (x1 <= x2) and (y1 <= y2):
            return Node(vals_grid, x1, y1, x2, y2)
        else:
            return None

    def _iter_existing_nodes(self):
        for node in (
            self.top_left, self.top_right, self.bottom_right, self.bottom_left
        ):
            if node:
                yield node

    @staticmethod
    def _calc_overlap_region_if_valid(node, x1, y1, x2, y2):
        sub_x1 = max(node.x1, x1)
        sub_y1 = max(node.y1, y1)
        sub_x2 = min(node.x2, x2)
        sub_y2 = min(node.y2, y2)

        if (sub_x1 <= sub_x2) and (sub_y1 <= sub_y2):
            return True, (sub_x1, sub_y1, sub_x2, sub_y2)
        return False, None


class GridMinMaxSegmentTree:
    def __init__(self, vals_grid):
        max_coord = len(vals_grid) - 1
        self.root = Node(vals_grid, 0, 0, max_coord, max_coord)

    def query_range_min_max(self, x1, y1, x2, y2):
        return self.root.query_range_min_max(x1, y1, x2, y2)

    def update_val(self, x, y, val):
        self.root.update_val(x, y, val)


def read_line():
    return sys.stdin.readline().strip()


def main():
    grid_size = int(read_line())
    vals_grid = [list(map(int, read_line().split())) for _ in range(grid_size)]

    min_max_tree = GridMinMaxSegmentTree(vals_grid)

    n_queries = int(read_line())
    for _ in range(n_queries):
        query_tokens = read_line().split()
        if query_tokens[0] == 'q':
            x1, y1, x2, y2 = (int(coord) - 1 for coord in query_tokens[1:])
            min_val, max_val = min_max_tree.query_range_min_max(x1, y1, x2, y2)
            print(f"{max_val} {min_val}")
        else:
            x, y = (int(coord) - 1 for coord in query_tokens[1:-1])
            val = int(query_tokens[-1])
            min_max_tree.update_val(x, y, val)

    return 0


if __name__ == '__main__':
    sys.exit(main())
