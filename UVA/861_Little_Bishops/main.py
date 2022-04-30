import pickle
import sys


def read_pair():
    return map(int, sys.stdin.readline().strip().split())


def get_attack_bitmasks(board_size):
    coord_modifs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
    attack_bitmasks = []

    for row in range(board_size):
        for col in range(board_size):
            attack_bitmask = 0

            for row_delta, col_delta in coord_modifs:
                curr_row, curr_col = row, col

                while (
                    (0 <= curr_row < board_size) and
                    (0 <= curr_col < board_size)
                ):
                    curr_pos = (curr_row * board_size) + curr_col
                    attack_bitmask |= 1 << curr_pos

                    curr_row += row_delta
                    curr_col += col_delta

            attack_bitmasks.append(attack_bitmask)

    return attack_bitmasks


def calc_bishop_solutions(board_size, n_bishops):
    if n_bishops == 0:
        return 1

    attack_bitmasks = get_attack_bitmasks(board_size)

    count = 0
    max_start_pos = board_size**2 - n_bishops + 1
    stack = [(pos, n_bishops, 0) for pos in range(max_start_pos)]

    while stack:
        pos, rem_bishops, occupations_bitmask = stack.pop()

        curr_attack_bitmask = attack_bitmasks[pos]
        if (occupations_bitmask & curr_attack_bitmask) > 0:
            continue

        if rem_bishops == 1:
            count += 1
        else:
            next_rem_bishops = rem_bishops - 1
            max_next_pos = board_size**2 - next_rem_bishops + 1
            new_occupations_bitmask = occupations_bitmask | (1 << pos)

            stack.extend(
                (next_pos, next_rem_bishops, new_occupations_bitmask)
                for next_pos in range(pos + 1, max_next_pos)
            )

    return count


def main():
    precalc_results = {}

    for board_size in range(1, 9):
        for n_bishops in range(board_size**2 + 1):
            print(f"computing: {board_size}, {n_bishops}")
            count = calc_bishop_solutions(board_size, n_bishops)
            precalc_results[(board_size, n_bishops)] = count

    with open('precalc_results.bin', 'wb') as out_file:
        pickle.dump(precalc_results, out_file)


if __name__ == '__main__':
    sys.exit(main())
