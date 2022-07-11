// g++ -Wall -Wextra -pedantic -O3 -s -std=c++11 -march=native -fno-rtti main.cpp -o main

#include <iostream>
#include <iomanip>
#include <cmath>
#include <cassert>

using namespace std;

typedef unsigned long long int n_t;

static const n_t kMaxNum(static_cast<n_t>(powl(10, 16)));
static const n_t kMod(kMaxNum);

static int digit_sum(const n_t &num, int base)
{
    register int sum = 0;
    register n_t curr_num(num);

    while (curr_num > 0)
    {
        sum += curr_num % base;
        curr_num /= base;
    }

    return sum;
}

static inline bool is_double_base_expressible(
    const n_t &num, int base_1, int base_2)
{
    return digit_sum(num, base_1) == digit_sum(num, base_2);
}

static n_t sum_double_expressible_nums(
    const n_t &max_num, int upper_base, int lower_base)
{
    n_t nums_sum(0);
    n_t curr_num(0);

    auto sum_formula_coef(lower_base >> 1);

    while (curr_num <= max_num)
    {
        if (is_double_base_expressible(curr_num, upper_base, lower_base))
        {
            nums_sum = (nums_sum + (((((curr_num << 1) % kMod) + (lower_base - 1)) % kMod) * sum_formula_coef) % kMod) % kMod;
        }

        curr_num += upper_base;
    }
    return nums_sum;
}

int main()
{
    assert(sum_double_expressible_nums(10, 8, 2) == 18);
    assert(sum_double_expressible_nums(100, 8, 2) == 292);
    assert(sum_double_expressible_nums(1000000, 8, 2) == 19173952);

    n_t nums_sum(0);

    for (int upper_base_exp = 3; upper_base_exp <= 6; ++upper_base_exp)
    {
        int upper_base = static_cast<int>(pow(2, upper_base_exp));

        for (
            int lower_base_exp = 1;
            lower_base_exp <= (upper_base_exp - 2);
            ++lower_base_exp)
        {
            int lower_base = static_cast<int>(pow(2, lower_base_exp));

            cout << "Processing bases " << upper_base << " and " << lower_base << endl;

            auto curr_sum(sum_double_expressible_nums(
                kMaxNum, upper_base, lower_base));
            nums_sum = (nums_sum + curr_sum) % kMod;
        }
    }

    cout << "Result: " << setfill('0') << setw(16) << nums_sum << endl;

    return 0;
}
