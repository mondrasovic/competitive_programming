import sys


def main():
    m = 50

    dp = [0] * (m + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[4] = 8

    for i in range(5, len(dp)):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]

    print(f"Solution: {dp[-1]}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
