import sys

sys.setrecursionlimit(2_000)

rows, _, max_steps_count = tuple(map(int, input().strip().split()))
grid = [list(input().strip()) for _ in range(rows)]
letter_coord_modifs = (
    ('U', (-1, 0)),
    ('D', (1, 0)),
    ('L', (0, -1)),
    ('R', (0, 1))
)

memo = {}

def find_min_changes_count(row, col, steps_count):
    stored_res = memo.get((row, col, steps_count))
    if stored_res is not None:
        return stored_res
    
    if (not (0 <= row < len(grid) and 0 <= col < len(grid[0]))) or (steps_count > max_steps_count):
        return sys.maxsize
    
    curr_letter = grid[row][col]
    if curr_letter == '*':
        return 0
    
    min_changes_count = sys.maxsize
    for new_letter, (row_modif, col_modif) in letter_coord_modifs:
        grid[row][col] = new_letter
        min_changes_count = min(
            min_changes_count,
            (1 * (new_letter != curr_letter)) + find_min_changes_count(
                row + row_modif,
                col + col_modif,
                steps_count + 1))
        grid[row][col] = curr_letter
        
        if min_changes_count == 0:
            break
    
    memo[(row, col, steps_count)] = min_changes_count
    
    return min_changes_count

res = find_min_changes_count(0, 0, 0)
print(res if res < sys.maxsize else -1)