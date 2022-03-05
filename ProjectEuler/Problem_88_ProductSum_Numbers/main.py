import sys


def find_factorizations(num):
    factorizations = []

    for div in range(2, num + 1):
        if (num % div) == 0:
            for sub_factorization in find_factorizations(num // div):
                factorizations.append([div] + sub_factorization)

    if not factorizations:
        factorizations.append([num])

    return factorizations


def main():
    max_num = 12_000
    min_product_sum = [i * 2 for i in range(max_num + 1)]

    for curr_prod in range(2, 2 * max_num + 1):
        for factorization in find_factorizations(curr_prod):
            curr_sum = sum(factorization)
            curr_k = len(factorization) + (curr_prod - curr_sum)
            if curr_k < len(min_product_sum):
                min_product_sum[curr_k] = min(
                    min_product_sum[curr_k], curr_prod
                )

    print(f"Result: {sum(set(min_product_sum[2:]))}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
