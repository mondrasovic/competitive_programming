import sys


def read_line():
    return sys.stdin.readline().strip()


def calc_sum_dist(locations, target_pos):
    return sum(abs(location - target_pos) for location in locations)


def calc_min_sum_dist(locations):
    locations.sort()

    mid_pos = len(locations) // 2
    median = locations[mid_pos]

    return calc_sum_dist(locations, median)


def main():
    n_cases = int(read_line())

    for _ in range(n_cases):
        locations = list(map(int, read_line().split()))[1:]
        print(calc_min_sum_dist(locations))

    return 0


if __name__ == '__main__':
    sys.exit(main())
