mod = 10 ** 9 + 7

digit_str = input().strip()

sum_dp = [0] * (len(digit_str) + 1)
curr_ten_pow, ten_pow_sum = 1, 1

for i in range(len(digit_str) - 1, -1, -1):
    sum_dp[i] = ((int(digit_str[i]) * ten_pow_sum) + sum_dp[i + 1]) % mod
    curr_ten_pow = (curr_ten_pow * 10) % mod
    ten_pow_sum = (ten_pow_sum + curr_ten_pow) % mod

res_sum = sum(sum_dp)
print(res_sum % mod)