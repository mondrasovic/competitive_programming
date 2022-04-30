import sys


def read_ints():
    for line in sys.stdin:
        yield int(line.strip())


def reverse_4_bytes(val):
    return int.from_bytes(
        int.to_bytes(val, 4, byteorder='little', signed=True),
        byteorder='big',
        signed=True
    )


for val in read_ints():
    print(f"{val} converts to {reverse_4_bytes(val)}")
