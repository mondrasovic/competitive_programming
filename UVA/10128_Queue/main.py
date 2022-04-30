import sys


def read_line():
    return sys.stdin.readline().strip()


def calc_perms_count(n_people, n_unblocked_left, n_unblocked_right):
    dp = [
        [[0] * (n_people + 1) for _ in range(n_people + 1)]
        for _ in range(n_people + 1)
    ]

    dp[1][1][1] = 1

    for n in range(2, n_people + 1):
        for p in range(1, n + 1):
            for r in range(1, n + 1):
                dp[n][p][r] = (
                    dp[n - 1][p - 1][r] + dp[n - 1][p][r - 1] +
                    (n - 2) * dp[n - 1][p][r]
                )

    return dp[n_people][n_unblocked_left][n_unblocked_right]


def main():
    n_cases = int(read_line())

    for _ in range(n_cases):
        tokens = read_line().split()
        n_people, n_unblocked_left, n_unblocked_right = map(int, tokens)
        print(calc_perms_count(n_people, n_unblocked_left, n_unblocked_right))

    return 0


if __name__ == '__main__':
    sys.exit(main())
