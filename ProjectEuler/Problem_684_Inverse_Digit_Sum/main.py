import sys


def geom_seq_sum_mod(n, q, mod):
    return ((1 - pow(q, n + 1, mod)) // (1 - q)) % mod


def min_digit_sum_num(digit_sum, mod):
    n_trail_nines, leading_digit = digit_sum // 9, digit_sum % 9

    trail_tens_sum = geom_seq_sum_mod(
        n_trail_nines - 1, 10, mod
    ) if n_trail_nines > 0 else 0
    num = (
        ((leading_digit * pow(10, n_trail_nines, mod)) % mod) +
        ((9 * trail_tens_sum) % mod)
    ) % mod

    return num


def iter_fib_nums(n):
    a, b = 0, 1

    for _ in range(n):
        c = a + b
        yield c
        a, b = b, c


def main():
    mod = 1_000_000_007

    nums_sum = 0

    for digit_sum in iter_fib_nums(90):
        min_num = min_digit_sum_num(digit_sum, mod)
        nums_sum = (nums_sum + min_num) % mod
    # for digit_sum in range(0, 21):
    #     min_num = min_digit_sum_num(digit_sum, mod)
    #     nums_sum = (nums_sum + min_num) % mod

    print(f"Result: {nums_sum}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
