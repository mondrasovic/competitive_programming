from sys import stdin

def merge_count_inv(left, right):
    n_left, n_right = len(left), len(right)
    output = [None] * (n_left + n_right)
    i = j = k = inv_count = 0

    while i < n_left and j < n_right:
        if left[i] <= right[j]:
            output[k] = left[i]
            i += 1
        else:
            output[k] = right[j]
            inv_count += n_left - i
            j += 1
        k += 1

    while i < n_left:
        output[k] = left[i]
        i += 1
        k += 1
    
    while j < n_right:
        output[k] = right[j]
        j += 1
        k += 1

    return output, inv_count

def merge_sort_count_inv(vals):
    n_vals = len(vals)
    if n_vals == 1:
        return vals, 0
    
    half_size = n_vals // 2
    left, right = vals[:half_size], vals[half_size:]
    left_sorted, left_inv_count = merge_sort_count_inv(left)
    right_sorted, right_inv_count = merge_sort_count_inv(right)
    both_merge, both_inv_count = merge_count_inv(
        left_sorted,
        right_sorted
    )
    inv_count = left_inv_count + right_inv_count + both_inv_count

    return both_merge, inv_count

n_cases = int(stdin.readline().strip())
for _ in range(n_cases):
    stdin.readline()
    vals = tuple(map(int, stdin.readline().strip().split()))
    print(merge_sort_count_inv(vals)[1])
