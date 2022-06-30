import collections
import functools


@functools.lru_cache(maxsize=10_000)
def is_prime(num):
    if (num == 2) or (num == 3):
        return True

    if (num < 2) or (num % 2 == 0) or (num % 3 == 0):
        return False

    div = 5

    while div**2 <= num:
        if (num % div == 0) or (num % (div + 2) == 0):
            return False

        div += 6

    return True


def gen_strong_right_trunc_harshad_numbers(limit):
    strong_right_trunc_harshad_nums = set()
    nums_queue = collections.deque(zip(range(1, 10), range(1, 10)))

    while True:
        num, digit_sum = nums_queue.popleft()

        if num > limit:
            return

        if ((num // 10) in strong_right_trunc_harshad_nums) and is_prime(num):
            yield num

        if num % digit_sum == 0:
            if is_prime(num // digit_sum):
                strong_right_trunc_harshad_nums.add(num)

            num_left_shifted = num * 10
            for digit in range(10):
                nums_queue.append((num_left_shifted + digit, digit_sum + digit))


print(sum(gen_strong_right_trunc_harshad_numbers(10**14)))
