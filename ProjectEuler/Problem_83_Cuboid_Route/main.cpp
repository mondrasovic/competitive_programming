#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long double n_t;

static const int kSolutionsCountLimit = 1000000;

static inline bool is_integer(const n_t &x)
{
    return abs(roundl(x) - x) < 1e-12;
}

static inline n_t calc_shortest_path_len(
    const n_t &w, const n_t &h, const n_t &d)
{
    register auto tmp(h + d);
    return sqrtl((w * w) + (tmp * tmp));
}

int main()
{
    int n_solutions = 0;
    int a = 1;

    while (n_solutions <= kSolutionsCountLimit)
    {
        for (int b = a; b > 0; --b)
        {
            for (int c = b; c > 0; --c)
            {
                auto min_shortest_path_len(
                    min({calc_shortest_path_len(a, b, c),
                         calc_shortest_path_len(b, a, c),
                         calc_shortest_path_len(c, a, b)}));
                if (is_integer(min_shortest_path_len))
                {
                    ++n_solutions;
                }
            }
        }

        ++a;
    }

    cout << "Solution: " << (a - 1) << endl;

    return 0;
}
