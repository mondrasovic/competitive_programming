import sys


def read_line():
    return sys.stdin.readline().strip()


n_test_cases = int(read_line())
sep = ''

for _ in range(n_test_cases):
    read_line()

    permutation = tuple(int(p) - 1 for p in read_line().split())
    values = read_line().split()
    out_values = [None] * len(values)

    for value, idx in zip(values, permutation):
        out_values[idx] = value + "\n"

    out_text = "".join(out_values)
    print(f"{sep}{out_text}", end="")
    sep = "\n"
