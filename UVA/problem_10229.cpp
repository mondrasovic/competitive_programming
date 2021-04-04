#include <iostream>

using namespace std;

typedef unsigned long long int n_t;

static void calc_fib_coefs(n_t n, n_t m, n_t *a, n_t *b, n_t *c, n_t *d)
{
    if (n == 0) {
        *a = *d = 1;
        *b = *c = 0;
    } else if (n == 1) {
        *b = *c = *d = 1;
        *a = 0;
    } else {
        n_t a_sub, b_sub, c_sub, d_sub;
        calc_fib_coefs(n / 2, m, &a_sub, &b_sub, &c_sub, &d_sub);

        *a = ((a_sub * a_sub) % m + (b_sub * c_sub) % m) % m;
        *b = ((a_sub * b_sub) % m + (b_sub * d_sub) % m) % m;
        *c = ((c_sub * a_sub) % m + (d_sub * c_sub) % m) % m;
        *d = ((c_sub * b_sub) % m + (d_sub * d_sub) % m) % m;

        if (n & 1) {
            n_t a_tmp = *a, b_tmp = *b, c_tmp = *c, d_tmp = *d;

            *a = c_tmp;
            *b = d_tmp;
            *c = (a_tmp + c_tmp) % m;
            *d = (b_tmp + d_tmp) % m;
        }
    }
}

static n_t calc_fib(n_t n, n_t m)
{
    if (n == 0)
        return 0;

    n_t a, b, c, d;
    calc_fib_coefs(n - 1, 1 << m, &a, &b, &c, &d);

    return d;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    n_t n, m;

    while (cin >> n >> m) {
        cout << calc_fib(n, m) << endl;
    }

    return 0;
}
