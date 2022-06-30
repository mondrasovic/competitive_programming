#include <cmath>
#include <iostream>
#include <unordered_set>

using namespace std;

typedef long long int n_t;

static const n_t kMaxPerimeter = 1000000000; // One billion.
// static const n_t kMaxPerimeter = 1000000; // One billion.
static unordered_set<n_t> square_nums_;

static inline bool is_integer(long double x)
{
    return abs(roundl(x) - x) < 1e-16;
}

static inline bool is_integer_area(const n_t &a, const n_t &b)
{
    // return (b % 4 == 0) && (square_nums_.count(4 * a * a - b * b) > 0);
    return is_integer((b / 4.0L) * sqrtl(4 * a * a - (b * b)));
}

static inline bool is_valid_case(const n_t &a, const n_t &b, n_t *perimeter)
{
    *perimeter = (a * 2) + b;
    return (*perimeter <= kMaxPerimeter) && is_integer_area(a, b);
}

int main()
{
    // for (n_t n = 1; (n * n) <= kMaxPerimeter; ++n)
    // {
    //     square_nums_.insert(n * n);
    // }

    n_t a = 2;
    n_t perimeters_sum = 0;

    for (;;)
    {
        n_t perimeter;
        if (is_valid_case(a, a - 1, &perimeter))
        {
            // cout << a << " " << a << " " << a - 1 << " = " << perimeter << endl;
            perimeters_sum += perimeter;
        }
        if (is_valid_case(a, a + 1, &perimeter))
        {
            // cout << a << " " << a << " " << a + 1 << " = " << perimeter << endl;
            perimeters_sum += perimeter;
        }
        if (((3 * a) - 1) > kMaxPerimeter)
        {
            break;
        }
        ++a;
    }

    cout << "Result: " << perimeters_sum << endl;

    return 0;
}
