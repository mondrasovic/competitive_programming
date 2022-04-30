import sys


def read_line():
    return sys.stdin.readline().strip()


def find_word_occurrence(grid, word):
    coord_modifs = (
        (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)
    )

    n_rows, n_cols, n_chars = len(grid), len(grid[0]), len(word)

    for i in range(n_rows):
        for j in range(n_cols):
            for delta_i, delta_j in coord_modifs:
                n_matches = 0
                ii, jj, k = i, j, 0

                while (
                    (0 <= ii < n_rows) and (0 <= jj < n_cols) and (k < n_chars)
                ):
                    if word[k] == grid[ii][jj]:
                        n_matches += 1
                        k += 1
                        ii += delta_i
                        jj += delta_j
                    else:
                        break

                if n_matches == n_chars:
                    return i, j

    raise RuntimeError()


def main():
    n_cases = int(read_line())
    case_sep = ""

    for _ in range(n_cases):
        read_line()

        n_rows = int(read_line().split()[0])
        grid = [read_line().lower() for _ in range(n_rows)]

        n_words = int(read_line())

        print(case_sep, end="")
        case_sep = "\n"

        for _ in range(n_words):
            word = read_line().lower()
            pos_row, pos_col = find_word_occurrence(grid, word)
            print(f"{pos_row + 1} {pos_col + 1}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
