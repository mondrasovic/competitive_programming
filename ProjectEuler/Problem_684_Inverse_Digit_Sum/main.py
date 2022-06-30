<<<<<<< HEAD
import sys


def min_digit_sum_num(digit_sum, mod):
    return (
        (((digit_sum % 9) + 1) * pow(10, (digit_sum // 9), mod) % mod) - 1 + mod
    ) % mod


def iter_fib_nums(n):
    a, b = 0, 1

=======
# def min_digit_sum_num(digit_sum):
#     num = ((digit_sum % 9) + 1) * pow(10, digit_sum // 9) - 1
#     return num


def min_digit_sum_num(digit_sum, mod):
    num = (
        (((digit_sum % 9) + 1) * pow(10, digit_sum // 9, mod) % mod) + mod - 1
    ) % mod
    return num


def iter_fib_seq(n):
    a, b = 0, 1
>>>>>>> 23f5be592baaa90bdba122c44a2dedfbe2cf22c9
    for _ in range(n):
        c = a + b
        yield c
        a, b = b, c


<<<<<<< HEAD
def main():
    mod = 1_000_000_007

    nums_sum = 0

    for digit_sum in iter_fib_nums(91):
        min_num = min_digit_sum_num(digit_sum, mod)
        nums_sum = (nums_sum + min_num) % mod
    # for digit_sum in range(0, 50):
    #     min_num = min_digit_sum_num(digit_sum, mod)
    #     nums_sum = (nums_sum + min_num) % mod

    print(f"Result: {nums_sum}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
=======
mod = 1_000_000_007
num_sum = 0

for digit_sum in range(50):
    min_num = min_digit_sum_num(digit_sum, mod)
    num_sum = (num_sum + min_num) % mod
    print(f"f({digit_sum}) = {min_num}")

# for digit_sum in iter_fib_seq(90):
#     min_num = min_digit_sum_num(digit_sum, mod)
#     num_sum = (num_sum + min_num) % mod
print(f"Result: {num_sum}")
# for n in iter_fib_seq(90):
#     print(n)
>>>>>>> 23f5be592baaa90bdba122c44a2dedfbe2cf22c9
