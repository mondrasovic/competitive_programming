import sys
from itertools import count, chain


def time_str_to_sec(time_str):
    return (int(time_str[:2]) * 60) + int(time_str[3:])


def sec_to_time_str(sec):
    n_hours, n_mins = sec // 60, sec % 60
    return f'{n_hours:02d}:{n_mins:02d}'


def duration_to_time_str(duration):
    n_hours, n_mins = duration // 60, duration % 60
    res_str = ''
    if n_hours > 0:
        res_str += str(n_hours) + ' hours and '
    res_str += str(n_mins) + ' minutes'
    return res_str


def iter_schedules():
    input_iter = iter(sys.stdin)
    while True:
        try:
            line = next(input_iter).strip()
        except StopIteration:
            break
        else:
            if not line:
                break
            n_blocks = int(line)
            yield (next(input_iter) for _ in range(n_blocks))


def main():
    for day_num, blocks_iter in zip(count(start=1), iter_schedules()):
        time_blocks = []

        for block_str in blocks_iter:
            start_time_str = block_str[:5]
            end_time_str = block_str[6:11]

            start_time = time_str_to_sec(start_time_str)
            end_time = time_str_to_sec(end_time_str)
            time_blocks.append((start_time, end_time))

        time_blocks.sort()

        longest_nap_duration = 0
        longest_nap_start_time = None
        prev_time = time_str_to_sec('10:00')
        latest_dummy_block = [(time_str_to_sec('18:00'), None)]

        for (start_time, end_time) in chain(time_blocks, latest_dummy_block):
            duration = start_time - prev_time
            if duration > longest_nap_duration:
                longest_nap_duration = duration
                longest_nap_start_time = prev_time
            prev_time = end_time

        start_time_str = sec_to_time_str(longest_nap_start_time)
        duration_str = duration_to_time_str(longest_nap_duration)

        print(
            f'Day #{day_num}: the longest nap starts at {start_time_str} and will last for {duration_str}.'
        )

    return 0


if __name__ == '__main__':
    sys.exit(main())
