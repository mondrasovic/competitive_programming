import sys


def flip(vals, pos):
    return list(reversed(vals[:pos + 1])) + vals[pos + 1:]


def find_stack_flips(stack_descr):
    bottom_pos = len(stack_descr) - 1
    flips = []

    while bottom_pos > 0:
        max_pos, max_elem = 0, stack_descr[0]
        for i in range(1, bottom_pos + 1):
            if stack_descr[i] > max_elem:
                max_pos, max_elem = i, stack_descr[i]

        if max_pos == bottom_pos:
            bottom_pos -= 1
        elif max_pos == 0:
            stack_descr = flip(stack_descr, bottom_pos)
            flips.append(len(stack_descr) - bottom_pos)
            bottom_pos -= 1
        else:
            stack_descr = flip(stack_descr, max_pos)
            flips.append(len(stack_descr) - max_pos)

    flips.append(0)

    return flips


def main():
    for stack_str in map(str.strip, sys.stdin):
        stack_descr = list(map(int, stack_str.split()))
        print(
            stack_str + "\n" +
            " ".join(map(str, find_stack_flips(stack_descr)))
        )

    return 0


if __name__ == '__main__':
    sys.exit(main())
