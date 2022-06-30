#Project Euler Problem 121

from math import factorial

n = 15
r = (n - 1) // 2
p = [1] + [0] * r
for k in range(n + 1):
    for i in range(r, 0, -1):
        p[i] += k * p[i - 1]

print("For", n, "turns, max prize fund =", int(factorial(n + 1) / sum(p)))
