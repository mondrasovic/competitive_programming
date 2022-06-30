from itertools import combinations, combinations_with_replacement, permutations
from operator import add, sub, mul, truediv


def is_positive_integer(x, eps=1e-12):
    return (x > 0) and (abs(round(x) - x) < eps)


def eval_diff_brackets_valid_vals(a, b, c, d, op_1, op_2, op_3):
    f_1 = lambda: op_2(op_1(a, b), op_3(c, d))  # (a @ b) @ (c @ d)
    f_2 = lambda: op_3(op_2(op_1(a, b), c), d)  # ((a @ b) @ c) @ d
    f_3 = lambda: op_3(op_1(a, op_2(b, c)), d)  # (a @ (b @ c)) @ d
    f_4 = lambda: op_1(a, op_3(op_2(b, c), d))  # a @ ((b @ c) @ d)
    f_5 = lambda: op_1(a, op_2(b, op_3(c, d)))  # a @ (b @ (c @ d))

    for f in (f_1, f_2, f_3, f_4, f_5):
        try:
            val = f()
        except ZeroDivisionError:
            continue
        else:
            if is_positive_integer(val):
                yield int(val)


def find_1_to_n_longest_seq_length(produced_vals):
    seq_len = 0
    prev_val = 0

    for val in sorted(produced_vals):
        diff = val - prev_val

        if diff == 1:
            seq_len += 1
        elif diff > 1:
            break

        prev_val = val

    return seq_len


all_digits = tuple(range(1, 10))
all_operators = (add, sub, mul, truediv)

max_seq_len = 0
max_seq_len_digits = ''

for curr_digits_set in combinations(all_digits, 4):
    produced_vals = []

    for curr_digits_perm in permutations(curr_digits_set):

        for curr_operators_set in combinations_with_replacement(
            all_operators, 3
        ):
            for curr_operators_perm in permutations(curr_operators_set):
                produced_vals.extend(
                    val for val in eval_diff_brackets_valid_vals(
                        *curr_digits_perm, *curr_operators_perm
                    )
                )

    curr_seq_len = find_1_to_n_longest_seq_length(produced_vals)
    if curr_seq_len > max_seq_len:
        max_seq_len = curr_seq_len
        max_seq_len_digits = curr_digits_set

print("".join(map(str, sorted(max_seq_len_digits))))
