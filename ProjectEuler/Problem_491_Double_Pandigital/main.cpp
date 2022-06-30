#include <cmath>
#include <iostream>
#include <unordered_map>

using namespace std;

typedef unsigned long long int n_t;

static n_t _count_double_pandigital_nums(
    int used_digits_mask, int alternating_sum, int pos,
    unordered_map<int, n_t> *memo)
{
    if (pos == 20)
    {
        return (abs(alternating_sum) % 11 == 0) ? 1 : 0;
    }

    int state = (alternating_sum << 20) | used_digits_mask;
    auto stored_res = memo->find(state);

    if (stored_res != memo->end())
    {
        return stored_res->second;
    }

    int start_digit = (pos == 0) ? 1 : 0;
    int sign = (pos % 2 == 0) ? 1 : -1;
    int new_pos = pos + 1;

    n_t count = 0;

    for (int digit = start_digit; digit <= 9; ++digit)
    {
        int digit_flag = 1 << digit;

        if (used_digits_mask & digit_flag)
        {
            digit_flag <<= 10;

            if (used_digits_mask & digit_flag)
            {
                continue;
            }
        }

        int new_used_digits_mask = used_digits_mask | digit_flag;
        int new_alternating_sum = alternating_sum + (sign * digit);

        count += _count_double_pandigital_nums(
            new_used_digits_mask, new_alternating_sum, new_pos, memo);
    }

    memo->insert({state, count});

    return count;
}

static n_t count_double_pandigital_nums()
{
    unordered_map<int, n_t> memo;

    memo.reserve(100000000);

    return _count_double_pandigital_nums(0, 0, 0, &memo);
}

int main()
{
    cout << "Result: " << count_double_pandigital_nums() << endl;

    return 0;
}
