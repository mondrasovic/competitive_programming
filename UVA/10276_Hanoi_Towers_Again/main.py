import math
import sys


def read_int():
    return int(sys.stdin.readline().strip())


def is_square(n, eps=1e-12):
    root = math.sqrt(n)
    return abs(round(root) - root) < eps


def find_max_peg_val(n_pegs):
    state = [0] * n_pegs
    ball_val = 1

    while True:
        expanded_at_zero = False

        for i in range(len(state)):
            curr_val = state[i]

            if curr_val == 0:
                if expanded_at_zero:
                    break
                expanded_at_zero = True
            else:
                if not is_square(curr_val + ball_val):
                    continue

            state[i] = ball_val
            ball_val += 1
            break
        else:
            break

    return ball_val - 1


def main():
    n_cases = read_int()

    for _ in range(n_cases):
        n_pegs = read_int()
        print(find_max_peg_val(n_pegs))

    return 0


if __name__ == '__main__':
    sys.exit(main())
