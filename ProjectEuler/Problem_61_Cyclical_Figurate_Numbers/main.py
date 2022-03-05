import sys


def is_integral(x, eps=1e-12):
    return abs(x - round(x)) < eps


def triangular(n):
    return (n * (n + 1)) // 2


def square(n):
    return n * n


def pentagonal(n):
    return (n * (3 * n - 1)) // 2


def hexagonal(n):
    return n * (2 * n - 1)


def heptagonal(n):
    return (n * (5 * n - 3)) // 2


def octagonal(n):
    return n * (3 * n - 2)


def is_cyclic_4digit_pair(a, b):
    return (a % 100) == (b // 100)


def are_digits_linked(n):
    return (1000 <= n <= 9999) and (n % 100 >= 10)


def main():
    num_generators = (
        triangular, square, pentagonal, hexagonal, heptagonal, octagonal
    )

    i = 1
    in_range = False
    nums = set()
    while True:
        curr_nums = set(
            filter(are_digits_linked, (gen(i) for gen in num_generators))
        )
        if len(curr_nums) == 0:
            if in_range:
                break
        else:
            in_range = True
            nums = nums | curr_nums
        i += 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
