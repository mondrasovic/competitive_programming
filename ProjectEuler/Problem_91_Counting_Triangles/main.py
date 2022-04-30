import sys


def is_triangle_valid(p_x, p_y, q_x, q_y):
    if p_x == q_x:
        if p_x == 0:
            return False
        if p_y == q_y:
            return False
    if p_y == q_y:
        if p_y == 0:
            return False

    p_norm = p_x**2 + p_y**2
    q_norm = q_x**2 + q_y**2
    pq_norm = (p_x - q_x)**2 + (p_y - q_y)**2

    return (
        (p_norm + q_norm == pq_norm) or (p_norm + pq_norm == q_norm) or
        (q_norm + pq_norm == p_norm)
    )


def count_integer_triangles(coord_limit):
    count = 0
    range_limit = coord_limit + 1

    for p_x in range(0, range_limit):
        for p_y in range(1, range_limit):
            for q_x in range(p_x, range_limit):
                for q_y in range(0, p_y + 1):
                    if is_triangle_valid(p_x, p_y, q_x, q_y):
                        count += 1

    return count


def main():
    coord_limit = 50
    triangle_count = count_integer_triangles(coord_limit)
    print(f"Solution for coord limit {coord_limit} = {triangle_count}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
