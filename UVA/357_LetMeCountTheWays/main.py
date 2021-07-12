from sys import stdin

max_val = 30_000
coins = (1, 5, 10, 25, 50)
dp = [0] * (max_val + 1)
dp[0] = 1

for c in coins:
    for n in range(1, len(dp)):
        dp[n] += (c <= n) * dp[n - c]

for n in map(int, stdin.readlines()):
    m = dp[n]
    ways = f"are {m} ways" if m > 1 else f"is only 1 way"
    print(f"There {ways} to produce {n} cents change.")
