#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

typedef unsigned long long int n_t;

static const size_t kMaxNum = 64000000;

static bool is_perfect_square(n_t num)
{
    auto root(sqrtl(static_cast<long double>(num)));
    return abs(root - roundl(root)) < 1e-12;
}

int main()
{
    vector<n_t> divs_square_sum(kMaxNum);

    n_t perfect_square_divs_sum = 0;

    for (n_t base = 1; base < divs_square_sum.size(); ++base)
    {
        auto base_sq(base * base);

        for (n_t div = base; div < divs_square_sum.size(); div += base)
        {
            divs_square_sum[div] += base_sq;
        }

        if (is_perfect_square(divs_square_sum[base]))
        {
            perfect_square_divs_sum += base;
        }
    }

    cout << "Result: " << perfect_square_divs_sum << endl;

    return 0;
}