from __future__ import annotations

import abc
import dataclasses


N_ITERS = 11_000
GRID_SIZE = 5_000
START_ROW = GRID_SIZE // 2
START_COL = GRID_SIZE // 2


@dataclasses.dataclass(frozen=True)
class CoordModif:
    row_modif: int
    col_modif: int


class Direction(abc.ABC):
    @abc.abstractmethod
    def move_forward(self) -> CoordModif:
        pass

    @abc.abstractmethod
    def turn_clockwise(self) -> Direction:
        pass

    @abc.abstractmethod
    def turn_counterclockwise(self) -> Direction:
        pass


class Up(Direction):
    def move_forward(self) -> CoordModif:
        return CoordModif(row_modif=-1, col_modif=0)

    def turn_clockwise(self) -> Direction:
        return Right()

    def turn_counterclockwise(self) -> Direction:
        return Left()


class Right(Direction):
    def move_forward(self) -> CoordModif:
        return CoordModif(row_modif=0, col_modif=1)

    def turn_clockwise(self) -> Direction:
        return Down()

    def turn_counterclockwise(self) -> Direction:
        return Up()


class Down(Direction):
    def move_forward(self) -> CoordModif:
        return CoordModif(row_modif=1, col_modif=0)

    def turn_clockwise(self) -> Direction:
        return Left()

    def turn_counterclockwise(self) -> Direction:
        return Right()


class Left(Direction):
    def move_forward(self) -> CoordModif:
        return CoordModif(row_modif=0, col_modif=-1)

    def turn_clockwise(self) -> Direction:
        return Up()

    def turn_counterclockwise(self) -> Direction:
        return Down()


class Position:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
    
    def update(self, coord_modif: CoordModif) -> None:
        self.row += coord_modif.row_modif
        self.col += coord_modif.col_modif


class Grid:
    def __init__(self, size: int) -> None:
        self.grid = [[True] * size for _ in range(size)]
        self.n_black_cells = 0
    
    def flip(self, position: Position) -> None:
        if self.grid[position.row][position.col]:
            self.n_black_cells += 1
        else:
            self.n_black_cells -= 1
        self.grid[position.row][position.col] = not self.grid[position.row][position.col]
    
    def is_white(self, position: Position) -> bool:
        return self.grid[position.row][position.col]


def main():
    grid = Grid(GRID_SIZE)
    position = Position(START_ROW, START_COL)
    direction = Up()
    n_black_cells_deltas = []
    n_black_cells_values = [0]

    for i in range(N_ITERS):
        if grid.is_white(position):
            direction = direction.turn_clockwise()
        else:
            direction = direction.turn_counterclockwise()
        grid.flip(position)
        coord_modif = direction.move_forward()
        position.update(coord_modif)
        n_black_cells_deltas.append(grid.n_black_cells - n_black_cells_values[-1])
        n_black_cells_values.append(grid.n_black_cells)

    period = 104
    index = 10000

    while True:
        first_part = n_black_cells_deltas[index:index + period]
        second_part = n_black_cells_deltas[index + period:index + 2 * period]
        if first_part == second_part:
            delta_pattern = first_part
            break
        index += 1
    
    target_iter = 10 ** 18
    base_count = n_black_cells_values[index]
    rem_n_iters = target_iter - index
    final_count = base_count + (rem_n_iters // period) * sum(delta_pattern) + sum(delta_pattern[:rem_n_iters % period])
    print(final_count)


if __name__ == "__main__":
    main()
