import sys


def count_block_combinations(row_size, min_block_size=3):
    memo = {}

    def _count_combinations_recurse(start_pos, rem_blocks_count):
        if rem_blocks_count <= 0:
            return 1

        memo_key = (start_pos, rem_blocks_count)
        res_count = memo.get(memo_key)
        if res_count is not None:
            return res_count

        res_count = 0
        for curr_start_pos in range(start_pos, row_size - min_block_size + 2):
            for size in range(min_block_size, row_size - curr_start_pos + 1):
                res_count += _count_combinations_recurse(
                    curr_start_pos + size + 1, rem_blocks_count - 1
                )

        memo[memo_key] = res_count

        return res_count

    max_count = (row_size + 1) // (min_block_size + 1)
    total_count = 0
    for count in range(max_count + 1):
        total_count += _count_combinations_recurse(0, count)

    return total_count


def main():
    assert count_block_combinations(7) == 17
    print(f"Solution: {count_block_combinations(50)}")
    return 0


if __name__ == '__main__':
    sys.exit(main())
