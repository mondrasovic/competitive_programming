import sys


def find_max_valid_magic_arrangement(
    digit_groups, digit_dependent_positions, min_val, max_val, arrangement_len
):
    n_groups, group_size = len(digit_groups), len(digit_groups[0])
    n_pos = n_groups * group_size
    n_vals = max_val - min_val + 1
    valid_arrangements = []
    used_digits = set()

    def _solve(pos):
        if pos == n_pos:
            min_group_pos = 0
            min_group = tuple(digit_groups[0])
            group_sum = sum(min_group)

            for i, digit_group in enumerate(digit_groups[1:], start=1):
                curr_sum = sum(digit_group)
                if curr_sum != group_sum:
                    return

                curr_group = tuple(digit_group)
                if curr_group < min_group:
                    min_group_pos, min_group = i, curr_group

            arrangement = ''.join(
                ''.join(map(str, digit_groups[i % n_groups]))
                for i in range(min_group_pos, n_groups + min_group_pos)
            )

            if len(arrangement) == arrangement_len:
                valid_arrangements.append(arrangement)
        else:
            group_idx = pos // group_size
            item_idx = pos % group_size

            next_pos = pos + 1

            if digit_groups[group_idx][item_idx] is None:
                digit_dependent_pos = (
                    digit_dependent_positions[group_idx][item_idx]
                )

                for digit in range(min_val, max_val + 1):
                    if digit in used_digits:
                        continue

                    digit_groups[group_idx][item_idx] = digit

                    if digit_dependent_pos is not None:
                        next_group_idx, next_item_idx = digit_dependent_pos
                        digit_groups[next_group_idx][next_item_idx] = digit

                    used_digits.add(digit)
                    _solve(next_pos)
                    used_digits.remove(digit)

                digit_groups[group_idx][item_idx] = None
            else:
                _solve(next_pos)

    _solve(0)
    max_arrangement = max(valid_arrangements)

    return max_arrangement


def main():
    digit_groups = (
        [None, None, None], [None, None, None], [None, None, None], [
            None, None, None
        ], [None, None, None]
    )
    digit_dependent_positions = (
        (None, (4, 2), (1, 1)), (None, None, (2, 1)), (None, None, (3, 1)),
        (None, None, (4, 1)), (None, None, None)
    )
    max_arrangement = find_max_valid_magic_arrangement(
        digit_groups, digit_dependent_positions, 1, 10, 16
    )
    print(f"Solution: {max_arrangement}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
