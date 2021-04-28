#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

static const int kMaxVal = 10000001 + 1;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> prime_factors_count(kMaxVal);
    vector<int> rem_val(kMaxVal);
    vector<int> fact_factors_count(kMaxVal);

    iota(rem_val.begin(), rem_val.end(), 0);

    for (int i = 2; i < kMaxVal; ++i) {
        if (rem_val[i] == i) {
            for (int j = i; j < kMaxVal; j += i) {
                while (rem_val[j] % i == 0) {
                    rem_val[j] /= i;
                    ++prime_factors_count[j];
                }
            }
        }

        fact_factors_count[i] =
            fact_factors_count[i - 1] + prime_factors_count[i];
    }

    int n_case = 0;
    int n_prime_factors;

    while ((cin >> n_prime_factors) && (n_prime_factors >= 0)) {
        auto begin(fact_factors_count.begin());
        auto end(fact_factors_count.end());
        auto factors_it(lower_bound(begin, end, n_prime_factors));

        cout << "Case " << (++n_case) << ": ";
        if (factors_it != end) {
            if (*factors_it == n_prime_factors) {
                auto pos = factors_it - begin;
                cout << pos << '!' << endl;
                continue;
            }
        }
        cout << "Not possible." << endl;
    }

    return 0;
}
