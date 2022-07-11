MAX_NUM = 10**16
MOD = 10**16


def digit_sum(num, base):
    ret_sum = 0

    while num > 0:
        ret_sum += num % base
        num //= base

    return ret_sum


def is_double_base_expressible(num, base_1, base_2):
    return digit_sum(num, base_1) == digit_sum(num, base_2)


def sum_double_base_expressible_nums(max_num, upper_base, lower_base):
    nums_sum = curr_num = 0

    sum_formula_add_coef = lower_base - 1
    sum_formula_mul_coef = lower_base >> 1

    while curr_num <= max_num:
        if is_double_base_expressible(curr_num, upper_base, lower_base):
            nums_sum = (
                nums_sum + (
                    (((curr_num << 1) % MOD + sum_formula_add_coef) % MOD) *
                    sum_formula_mul_coef
                ) % MOD
            ) % MOD

        curr_num += upper_base

    return nums_sum


assert digit_sum(9, 2) == 2

assert is_double_base_expressible(17, 4, 2)


def print_double_base_expressible_nums(max_num, upper_base, lower_base):
    for num in range(max_num + 1):
        if is_double_base_expressible(num, upper_base, lower_base):
            print(num)


assert sum_double_base_expressible_nums(10, 8, 2) == 18
assert sum_double_base_expressible_nums(100, 8, 2) == 292
assert sum_double_base_expressible_nums(10**6, 8, 2) == 19_173_952

# MAX_NUM = 10**16
# MOD = 10**16

# nums_sum = 0

# for upper_base_exp in range(3, 7):
#     upper_base = 2**upper_base_exp

#     for lower_base_exp in range(1, upper_base_exp - 1):
#         lower_base = 2**lower_base_exp

#         nums_sum = (
#             nums_sum +
#             sum_double_base_expressible_nums(MAX_NUM, upper_base, lower_base)
#         ) % MOD

# print(f"{nums_sum:016d}")