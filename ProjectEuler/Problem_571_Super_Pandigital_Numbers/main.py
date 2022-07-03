def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]

    arr[i:] = arr[len(arr) - 1:i - 1:-1]

    return True


def is_base_pandigital(num, base):
    digit_occur_mask = 0

    while num > 0:
        digit_occur_mask |= (1 << (num % base))
        num //= base

    return digit_occur_mask == (1 << base) - 1


def is_n_super_pandigital(num, n_bases):
    return all(
        is_base_pandigital(num, base) for base in range(n_bases - 1, 2, -1)
    )


def str_arr_to_int(num_arr, src_base):
    num = 0

    for digit in num_arr:
        num = (num * src_base) + digit

    return num


assert str_arr_to_int([1, 2, 4, 0, 3], 5) == 978
assert str_arr_to_int([3, 3, 1, 0, 2], 4) == 978
assert str_arr_to_int([1, 1, 0, 0, 0, 2, 0], 3) == 978

assert is_base_pandigital(978, 2)
assert is_base_pandigital(978, 3)
assert is_base_pandigital(978, 4)
assert is_base_pandigital(978, 5)

assert is_n_super_pandigital(978, 5)
assert is_n_super_pandigital(1093265784, 10)

num_arr = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
n_bases = 12

smallest_nums = []

while len(smallest_nums) < 10:
    curr_num = str_arr_to_int(num_arr, src_base=n_bases)

    if is_n_super_pandigital(curr_num, n_bases):
        smallest_nums.append(curr_num)

    next_permutation(num_arr)

print(f"Result: {sum(smallest_nums)}")
