mod = 1_000_000_007
max_height = max_width = 1000

row_combs = [1] * (max_width + 1)
row_combs[2] = 2
row_combs[3] = 4
for i in range(4, len(row_combs)):
    row_combs[i] = sum(row_combs[i - 4:i]) % mod

solid_walls = [[1] * (max_width + 1) for _ in range(max_height + 1)]
all_walls = [[1] * (max_width + 1) for _ in range(max_height + 1)]

for j in range(2, len(all_walls[0])):
    combs = row_combs[j]
    for i in range(1, len(all_walls)):
        coef = combs * (i % 2 == 1) + 1 * (i % 2 == 0)
        all_walls[i][j] = (pow(all_walls[i // 2][j], 2, mod) * coef) % mod

for i in range(1, len(solid_walls)):
    for j in range(2, len(solid_walls[i])):
        invalid_walls = sum(
            (solid_walls[i][k] * all_walls[i][j - k]) % mod
            for k in range(1, j)) % mod
        solid_walls[i][j] = (all_walls[i][j] - invalid_walls + mod) % mod

for _ in range(int(input())):
    height, width = tuple(map(int, input().split()))
    print(solid_walls[height][width])
