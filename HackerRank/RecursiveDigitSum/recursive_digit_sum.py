n, k = input().split()

def super_digit(n):
    if n < 10:
        return n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return super_digit(s)

print(super_digit(sum(map(int, n)) * int(k)))