n = 6

def binary_search(a, b, i):
    m = a + (b - a) // 2
    m = (a + b) // 2
    sep = ' ' * i
    print(f'{sep}{a} {b} {m}')
    if a < b:
        binary_search(a, m, i + 1)
        binary_search(m + 1, b, i + 1)

binary_search(0, n - 1, 0)
