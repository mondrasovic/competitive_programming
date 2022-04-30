import sys


def read_line():
    return sys.stdin.readline().strip()


curr_case = 1

while True:
    values = read_line()
    if len(values) == 0:
        break

    print(f"Case {curr_case}:")
    n_queries = int(read_line())
    for _ in range(n_queries):
        tokens = read_line().split()
        lower, upper = tuple(map(int, tokens))
        if lower > upper:
            lower, upper = upper, lower

        for i in range(lower + 1, upper + 1):
            if values[i - 1] != values[i]:
                print("No")
                break
        else:
            print("Yes")

    curr_case += 1
