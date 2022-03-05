import math


def find_nth_2_pow_with_leading_digits(digits, n):
    n_digits = int(math.ceil(math.log10(digits)))
    log_10_2 = math.log10(2.0)
    curr_log_val = log_10_2
    curr_pow = n_vals = 1

    while True:
        dec_part = curr_log_val - math.floor(curr_log_val)
        exp_dec_part = math.pow(10.0, dec_part)
        leading_digits = int(exp_dec_part * math.pow(10.0, n_digits - 1))
        if leading_digits == digits:
            if n_vals == n:
                break
            n_vals += 1
        curr_log_val += log_10_2
        curr_pow += 1

    return curr_pow


assert find_nth_2_pow_with_leading_digits(12, 1) == 7
assert find_nth_2_pow_with_leading_digits(12, 2) == 80
assert find_nth_2_pow_with_leading_digits(123, 45) == 12710

print(find_nth_2_pow_with_leading_digits(123, 678910))
