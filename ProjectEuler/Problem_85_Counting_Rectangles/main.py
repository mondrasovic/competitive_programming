import sys


def main():
    target_count_val = 2_000_000
    max_size = int(target_count_val**0.5)

    dp = [[0 for _ in range(max_size)] for _ in range(max_size)]

    min_diff_count = sys.maxsize
    min_diff_area = None

    for i in range(1, len(dp)):
        prev_i = i - 1

        for j in range(i, len(dp[i])):
            prev_j = j - 1
            area = i * j

            count = dp[i][j] = dp[j][i] = (
                dp[prev_i][j] + dp[i][prev_j] - dp[prev_i][prev_j] + area
            )

            count_diff = abs(target_count_val - count)
            if count_diff < min_diff_count:
                min_diff_count, min_diff_area = count_diff, area

    print(f"Solution: {min_diff_area}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
