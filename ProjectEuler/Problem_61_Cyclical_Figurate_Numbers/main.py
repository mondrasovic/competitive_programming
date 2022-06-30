import sys


<<<<<<< HEAD
def is_integral(x, eps=1e-12):
    return abs(x - round(x)) < eps


=======
>>>>>>> 23f5be592baaa90bdba122c44a2dedfbe2cf22c9
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


<<<<<<< HEAD
def is_cyclic_4digit_pair(a, b):
    return (a % 100) == (b // 100)


def are_digits_linked(n):
    return (1000 <= n <= 9999) and (n % 100 >= 10)


=======
def are_digits_linked(a, b):
    return (a % 100) == (b // 100)


def is_number_valid(n):
    return (1000 <= n <= 9999) and (n % 100 >= 10)


def find_figurate_num_cycle(num_items, succ_num_items, cycle_len):
    used_values = set()
    used_types = set()
    first_value = None

    def _solve_recurse(pos, num_item):
        next_pos = pos + 1
        num_val, num_type = num_item

        if next_pos < cycle_len:
            if (num_type in used_types) or (num_val in used_values):
                return False

            used_values.add(num_val)
            used_types.add(num_type)
        else:
            if are_digits_linked(num_val,
                                 first_value) and (num_type not in used_types):
                used_values.add(num_val)
                used_types.add(num_type)
                return True
            else:
                return False

        for succ_num_item in succ_num_items.get(num_item, []):
            if _solve_recurse(next_pos, succ_num_item):
                return True

        used_values.remove(num_val)
        used_types.remove(num_type)

        return False

    for num_item in num_items:
        used_values.clear()
        used_types.clear()
        first_value = num_item[0]

        if _solve_recurse(0, num_item):
            return used_values

    return None


>>>>>>> 23f5be592baaa90bdba122c44a2dedfbe2cf22c9
def main():
    num_generators = (
        triangular, square, pentagonal, hexagonal, heptagonal, octagonal
    )

<<<<<<< HEAD
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
=======
    num_items = set()
    for i in range(19, 142):
        for num_type, num_generator in enumerate(num_generators):
            num_val = num_generator(i)
            if is_number_valid(num_val):
                num_items.add((num_val, num_type))

    succ_num_items = {}

    for num_item_a in num_items:
        num_val_a, num_type_a = num_item_a

        for num_item_b in num_items:
            num_val_b, num_type_b = num_item_b

            if (
                (num_val_a != num_val_b) and (num_type_a != num_type_b) and
                are_digits_linked(num_val_a, num_val_b)
            ):
                curr_succ_items = succ_num_items.setdefault(num_item_a, [])
                curr_succ_items.append(num_item_b)

    num_cycle = find_figurate_num_cycle(num_items, succ_num_items, 6)
    if num_cycle is None:
        print(f"Cycle not found.")
    else:
        print(f"Cycle: {num_cycle} | Sum: {sum(num_cycle)} ")
>>>>>>> 23f5be592baaa90bdba122c44a2dedfbe2cf22c9

    return 0


if __name__ == '__main__':
    sys.exit(main())
