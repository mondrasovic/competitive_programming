import sys


def main():
    total_count_limit = 10**12

    blue_count, total_count = 85, 120
    while total_count <= total_count_limit:
        blue_count, total_count = (
            3 * blue_count + 2 * total_count - 2,
            4 * blue_count + 3 * total_count - 3
        )
    print(f"Blue count: {blue_count}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
