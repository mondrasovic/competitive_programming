import sys

sys.setrecursionlimit(20_000)

for _ in range(int(input())):
    input()
    vals = tuple(map(int, input().split()))

    partial_sums = [0] * (len(vals) + 1)
    for i, val in enumerate(vals):
        partial_sums[i + 1] = partial_sums[i] + val
    
    memo = {}
    def calc_max_score(i, j):
        stored_val = memo.get((i, j))
        if stored_val is not None:
            return stored_val
        
        score = 0
        for k in range(i, j):
            sum_left = partial_sums[k + 1] - partial_sums[i]
            sum_right = partial_sums[j + 1] - partial_sums[k + 1]
            if sum_left == sum_right:
                score = max(
                    score,
                    1 + max(calc_max_score(i, k), calc_max_score(k + 1, j)))
        
        memo[(i, j)] = score
        
        return score
    
    print(calc_max_score(0, len(vals) - 1))
