import collections
import operator
import sys


def iter_string_pairs():
    pair = []

    for line in sys.stdin:
        pair.append(line.strip())

        if len(pair) == 2:
            yield pair[0], pair[1]
            pair.clear()


def find_common_perm(str_1, str_2):
    letter_counts_1 = collections.Counter(str_1)
    letter_counts_2 = collections.Counter(str_2)
    if len(str_1) > len(str_2):
        letter_counts_1, letter_counts_2 = letter_counts_2, letter_counts_1

    res_perm = ''

    for letter, count_1 in sorted(
        letter_counts_1.items(), key=operator.itemgetter(0)
    ):
        res_perm += letter * min(count_1, letter_counts_2[letter])

    return res_perm


def main():
    for str_1, str_2 in iter_string_pairs():
        print(find_common_perm(str_1, str_2))

    return 0


if __name__ == '__main__':
    sys.exit(main())
