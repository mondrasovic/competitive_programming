import math

MAX_NUM = 64_000_000


def is_perfect_square(num, eps=1e-12):
    root = math.sqrt(num)
    return abs(root - round(root)) < eps


perfect_square_divs_sum = 0

divs_square_sum = [0] * MAX_NUM

for base in range(1, len(divs_square_sum)):
    base_sq = base * base

    for div in range(base, len(divs_square_sum), base):
        divs_square_sum[div] += base_sq

    if is_perfect_square(divs_square_sum[base]):
        perfect_square_divs_sum += base

print(perfect_square_divs_sum)