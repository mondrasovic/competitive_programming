from sys import stdin

max_n = 30
dp_a, dp_b = [0] * (max_n + 1), [0] * (max_n + 1)
dp_a[0] = dp_b[1] = 1

for i in range(2, len(dp_a)):
    dp_a[i] = dp_a[i - 2] + 2 * dp_b[i - 1]
    dp_b[i] = dp_a[i - 1] + dp_b[i - 2]

for n in filter(lambda n: n >= 0, map(int, stdin.readlines())):
    print(dp_a[n])
