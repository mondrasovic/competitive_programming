from sys import stdin

letters = (
    (".***..", "*...*.", "*****.", "*...*.", "*...*."),  # A
    ("****..", "*...*.", "****..", "*...*.", "****.."),  # B
    (".****.", "*...*.", "*.....", "*.....", ".****."),  # C
    ("****..", "*...*.", "*...*.", "*...*.", "****.."),  # D
    ("*****.", "*.....", "***...", "*.....", "*****."),  # E
    ("*****.", "*.....", "***...", "*.....", "*....."),  # F
    (".****.", "*.....", "*..**.", "*...*.", ".***.."),  # G
    ("*...*.", "*...*.", "*****.", "*...*.", "*...*."),  # H
    ("*****.", "..*...", "..*...", "..*...", "*****."),  # I
    ("..***.", "...*..", "...*..", "*..*..", ".**..."),  # J
    ("*...*.", "*..*..", "***...", "*..*..", "*...*."),  # K
    ("*.....", "*.....", "*.....", "*.....", "*****."),  # L
    ("*...*.", "**.**.", "*.*.*.", "*...*.", "*...*."),  # M
    ("*...*.", "**..*.", "*.*.*.", "*..**.", "*...*."),  # N
    (".***..", "*...*.", "*...*.", "*...*.", ".***.."),  # O
    ("****..", "*...*.", "****..", "*.....", "*....."),  # P
    (".***..", "*...*.", "*...*.", "*..**.", ".****."),  # Q
    ("****..", "*...*.", "****..", "*..*..", "*...*."),  # R
    (".****.", "*.....", ".***..", "....*.", "****.."),  # S
    ("*****.", "*.*.*.", "..*...", "..*...", ".***.."),  # T
    ("*...*.", "*...*.", "*...*.", "*...*.", ".***.."),  # U
    ("*...*.", "*...*.", ".*.*..", ".*.*..", "..*..."),  # V
    ("*...*.", "*...*.", "*.*.*.", "**.**.", "*...*."),  # W
    ("*...*.", ".*.*..", "..*...", ".*.*..", "*...*."),  # X
    ("*...*.", ".*.*..", "..*...", "..*...", "..*..."),  # Y
    ("*****.", "...*..", "..*...", ".*....", "*****."),  # Z
)

grid_size = 60
grid = None
init_new = True

def print_content():
    print("\n".join("".join(row) for row in grid))
    print("\n" + ("-" * grid_size) + "\n")
    

def grid_set_letter(row, col, letter):
    if (0 <= row < grid_size) and (0 <= col < grid_size):
        grid[row][col] = letter

def write_text(font, row, col, text):
    if font == 'C1':
        for i, letter in enumerate(text):
            if letter != " ":
                grid_set_letter(row, col + i, letter)
    else:  # C5
        col_start = 0
        for letter in text:
            if letter != " ":
                idx = ord(letter) - ord('A')
                ascii_art = letters[idx]
                for i in range(5):
                    for j in range(6):
                        symbol = ascii_art[i][j]
                        if symbol != ".":
                            grid_set_letter(row + i, col + col_start + j, symbol)
            col_start += 6


def calc_text_col_span(text, font):
    return len(text) * (1 if font == "C1" else 6)


for line in map(lambda s: s.strip()[1:], stdin.readlines()):
    if init_new:
        grid = [["."] * grid_size for _ in range(grid_size)]
        init_new = False
    
    str_arg_start_pos = line.find("|")
    if str_arg_start_pos >= 0:
        str_arg_end_pos = line.rfind("|")
        text = line[str_arg_start_pos + 1:str_arg_end_pos]
        tokens = line[:str_arg_start_pos].split()
        command, font = tokens[:2]
        row = int(tokens[2]) - 1
        
        if command == "C":
            col = (grid_size // 2) - (calc_text_col_span(text, font) // 2)
        elif command == "L":
            col = 0
        elif command == "R":
            col = grid_size - calc_text_col_span(text, font)
        else:  # P
            col = int(tokens[3]) - 1
        
        write_text(font, row, col, text)
    else:  # EOP
        print_content()
        init_new = True
