from sys import stdin

symbol_to_val = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
}
vals_symbols = (
    (1000, 'M'), (900, 'CM'), (500, 'D'),
    (400, 'CD'), (100, 'C'), (90, 'XC'), 
    (50, 'L'), (40, 'XL'), (10, 'X'),
    (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
)

def dec_to_roman(num):
    res = ''
    for val, symbol in vals_symbols:
        res += symbol * (num // val)
        num %= val
    return res

def roman_to_dec(num):
    res = i = 0
    while i < len(num):
        curr_val = symbol_to_val[num[i]]
        res += curr_val
        if (i + 1) < len(num):
            next_val = symbol_to_val[num[i + 1]]
            if curr_val < next_val:
                res += next_val - 2 * curr_val
                i += 1
        i += 1
    return res

for val in map(str.strip, stdin.readlines()):
    print(dec_to_roman(int(val)) if val.isdigit() else roman_to_dec(val))
