import itertools
from labmath import primegen, primepi


def count_numbers_with_8_divisors(max_val: int) -> int:
    primes: list[int] = list(primegen(max_val // 8))

    return (
        _single_prime_case(max_val, primes) +
        _double_prime_case(max_val, primes) +
        _triple_prime_case(max_val, primes)
    )


def _single_prime_case(max_val: int, primes: list[int]) -> int:
    return sum(1 for _ in itertools.takewhile(lambda p: p ** 7 <= max_val, primes))


def _double_prime_case(max_val: int, primes: list[int]) -> int:
    count: int = 0

    for p_1 in primes:
        p_1_cubed: int = p_1 ** 3
        if p_1_cubed > max_val:
            break

        for p_2 in primes:
            if p_2 == p_1:
                continue
            val: int = p_1_cubed * p_2
            if val > max_val:
                break
            count += 1
    
    return count


def _triple_prime_case(max_val: int, primes: list[int]) -> int:
    count: int = 0

    for i, p_1 in enumerate(primes):
        if p_1 ** 3 > max_val:
            break

        for j in range(i + 1, len(primes)):
            p_2: int = primes[j]
            max_p_3: int = max_val // (p_1 * p_2)
            if max_p_3 <= p_2:
                break
            count += primepi(max_p_3) - (j + 1)
    
    return count


def main() -> None:
    assert count_numbers_with_8_divisors(100) == 10
    assert count_numbers_with_8_divisors(1000) == 180
    assert count_numbers_with_8_divisors(1_000_000) == 224427
    # print(f"Solution: {count_numbers_with_8_divisors(10 ** 12)}")


if __name__ == "__main__":
    main()
