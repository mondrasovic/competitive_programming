from decimal import Decimal, getcontext

MAX_PERIMETER = 1_000_000_000

getcontext().prec = 50


def has_integer_area(a, b):
    area = (Decimal(b) / 4) * Decimal(4 * a * a - b * b).sqrt()
    return abs(area - area.to_integral_value()) < 1e-16


a = 2
perimeters_sum = 0

while True:
    b = a - 1
    perimeter = (2 * a) + b
    if perimeter <= MAX_PERIMETER:
        if has_integer_area(a, b):
            print(f"{a} {a} {b} = {perimeter}")
            perimeters_sum += perimeter

    b = a + 1
    perimeter = (2 * a) + b
    if perimeter <= MAX_PERIMETER:
        if has_integer_area(a, b):
            print(f"{a} {a} {b} = {perimeter}")
            perimeters_sum += perimeter
    else:
        break

    a += 1
