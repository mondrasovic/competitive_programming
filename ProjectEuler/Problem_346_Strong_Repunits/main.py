import collections
import itertools

# Every n is a 2-digit repunit in base n-1. So sum all distinct in-range
# repunits with 3 or more digits.  Add 1, which is a repunit in every base.

num_val_limit = 1_000_000_000_000

strong_repunits = {1}
for num_length in range(3, num_val_limit.bit_length() + 1):

    for base in itertools.count(2):
        curr_num = (base**num_length - 1) // (base - 1)
        if curr_num >= num_val_limit:
            break

        strong_repunits.add(curr_num)

repunit_nums_sum = sum(strong_repunits)

print(f"Repunit numbers sum: {repunit_nums_sum}")