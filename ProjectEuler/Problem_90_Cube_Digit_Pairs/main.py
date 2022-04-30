import itertools
import sys


def count_valid_digit_set_pairs(digit_sets):
    square_nums = (
        (0, 1), (0, 4), (0, 6), (1, 6), (2, 5), (3, 6), (4, 6), (8, 1)
    )
    count = 0

    for digit_set_a, digit_set_b in itertools.combinations(digit_sets, 2):
        is_valid = True
        for digit_tens, digit_ones in square_nums:
            if not (
                ((digit_tens in digit_set_a) and (digit_ones in digit_set_b)) or
                ((digit_tens in digit_set_b) and (digit_ones in digit_set_a))
            ):
                is_valid = False
                break

        if is_valid:
            count += 1

    return count


def main():
    digit_sets = itertools.combinations((0, 1, 2, 3, 4, 5, 6, 7, 8, 6), 6)
    valid_digit_pairs_count = count_valid_digit_set_pairs(digit_sets)
    print(f"Solution: {valid_digit_pairs_count}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
