max_n = 40

combs_num = [1] * (max_n + 1)
combs_num[4] = 2
for i in range(4, len(combs_num)):
    combs_num[i] = combs_num[i - 1] + combs_num[i - 4]

max_combs_num = combs_num[-1]
is_prime = [True] * (max_combs_num + 1)
is_prime[0] = is_prime[1] = False

for i in range(int(len(is_prime) ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, len(is_prime), i):
            is_prime[j] = False

primes_num = [0] * len(is_prime)
for i in range(1, len(primes_num)):
    primes_num[i] = primes_num[i - 1] + (1 * is_prime[i])

for _ in range(int(input())):
    n = int(input())
    print(primes_num[combs_num[n]])
