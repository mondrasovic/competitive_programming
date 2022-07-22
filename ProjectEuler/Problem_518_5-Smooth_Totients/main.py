import heapq


def gen_product_pow_combinations(vals, limit):
    visited = set()
    vals_queue = list(vals)
    heapq.heapify(vals_queue)

    while True:
        curr_val = heapq.heappop(vals_queue)
        if curr_val > limit:
            break

        if curr_val in visited:
            continue
        visited.add(curr_val)
        yield curr_val

        for val in vals:
            heapq.heappush(vals_queue, curr_val * val)


def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0) or (num % 3 == 0):
        return False

    div = 5

    while div**2 <= num:
        if (num % div == 0) or (num % (div + 2) == 0):
            return False

        div += 6

    return True


def gen_hamming_nums(limit):
    yield from gen_product_pow_combinations((2, 3, 5), limit)


def gen_hamming_succ_primes(hamming_nums, limit):
    yield from (
        succ for succ in map(lambda x: x + 1, hamming_nums)
        if (succ <= limit) and is_prime(succ)
    )


def gen_products(vals, limit):
    vals = sorted(vals)
    products = []
    curr_prod = 1

    def _search_recurse(index):
        nonlocal curr_prod

        curr_val = vals[index]
        new_prod = curr_prod * curr_val
        if new_prod > limit:
            return

        curr_prod = new_prod
        products.append(curr_prod)

        for next_index in range(index + 1, len(vals)):
            _search_recurse(next_index)

        curr_prod //= curr_val

    for i in range(len(vals)):
        _search_recurse(i)

    return products


def sum_5_smooth_totients(limit, mod=2**32):
    hamming_nums = list(gen_hamming_nums(limit))
    hamming_primes = list(gen_hamming_succ_primes(hamming_nums, limit))

    result = 0

    for prime_product in gen_products(hamming_primes, limit):
        result = (result + prime_product) % mod

        for hamming_num in hamming_nums:
            prime_hamming_prod = prime_product * hamming_num
            if prime_hamming_prod > limit:
                break
            result = (result + prime_hamming_prod) % mod

    return result


print(sum_5_smooth_totients(10))
assert sum_5_smooth_totients(10) == 55

result = 0
print(f"Result: {result}")