input_str = input()
lpss_dp = [[0] * (len(input_str) + 2) for _ in range(len(input_str) + 2)]

for i in range(len(input_str), 0, -1):
    for j in range(i, len(input_str) + 1):
        lpss_dp[i][j] = lpss_dp[i + 1][j - 1]
        if input_str[i - 1] == input_str[j - 1]:
            lpss_dp[i][j] = lpss_dp[i][j] + 1 + 1 * (i != j)
        lpss_dp[i][j] = max(lpss_dp[i][j], lpss_dp[i + 1][j], lpss_dp[i][j - 1])

print(max(lpss_dp[1][i] * lpss_dp[i + 1][len(input_str)]
    for i in range(1, len(input_str) + 1)))
