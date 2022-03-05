#include <iostream>
#include <cmath>

using namespace std;

static int find_nth_2_pow_with_leading_digits(int digits, int n)
{
    int n_digits = static_cast<int>(ceil(log10(digits)));
    long double log_10_2 = log10l(2.0);
    int curr_pow = 1;
    int n_vals = 1;

    while (true)
    {
        long double curr_log_val = curr_pow * log_10_2;
        long double dec_part = curr_log_val - floorl(curr_log_val);
        long double exp_dec_part = powl(10.0, dec_part);
        int leading_digits = static_cast<int>(
            exp_dec_part * powl(10.0, n_digits - 1));
        if (leading_digits == digits)
        {
            if (n_vals == n)
            {
                break;
            }
            ++n_vals;
        }
        ++curr_pow;
    }

    return curr_pow;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cout << find_nth_2_pow_with_leading_digits(12, 1) << endl;
    cout << find_nth_2_pow_with_leading_digits(12, 2) << endl;
    cout << find_nth_2_pow_with_leading_digits(123, 45) << endl;
    cout << find_nth_2_pow_with_leading_digits(123, 678910) << endl;

    return 0;
}
