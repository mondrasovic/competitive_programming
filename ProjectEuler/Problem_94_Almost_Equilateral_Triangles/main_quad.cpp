// #include <cmath>
#include <iostream>
#include <quadmath.h>

using namespace std;

typedef long long int n_t;
typedef __float128 f_t;

static const n_t kMaxPerimeter = 1000000000; // One billion.
// static const n_t kMaxPerimeter = 1000000; // One billion.

static inline bool is_integer(const f_t &x)
{
    return cabsq(roundq(x) - x) < 1e-16;
}

static inline bool is_integer_area(const n_t &a, const n_t &b)
{
    return is_integer((static_cast<f_t>(b) / static_cast<f_t>(4.0)) * sqrtq(4 * a * a - (b * b)));
}

static inline bool is_valid_case(const n_t &a, const n_t &b, n_t *perimeter)
{
    *perimeter = (a * 2) + b;
    return (*perimeter <= kMaxPerimeter) && is_integer_area(a, b);
}

int main()
{
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
