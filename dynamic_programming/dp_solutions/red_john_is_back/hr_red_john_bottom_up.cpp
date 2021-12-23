#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

static const int kMaxNum = 40;
typedef unsigned long long n_t;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n_cases;
    cin >> n_cases;

    vector<n_t> combs_num(kMaxNum + 1, 1);

    for (size_t i = 4; i < combs_num.size(); ++i) {
        combs_num[i] = combs_num[i - 1] + combs_num[i - 4];
    }

    vector<bool> is_prime(combs_num[kMaxNum] + 1, true);
    is_prime[0] = is_prime[1] = false;

    for (size_t i = 2; i <= static_cast<size_t>(sqrt(is_prime.size())); ++i) {
        if (is_prime[i]) {
            for (size_t j = i * i; j < is_prime.size(); j += i) {
                is_prime[j] = false;
            }
        }
    }

    vector<n_t> primes_num(is_prime.size(), 0);
    for (size_t i = 1; i < primes_num.size(); ++i) {
        primes_num[i] = primes_num[i - 1] + (1 * is_prime[i]);
    }

    for (int i = 0; i < n_cases; ++i) {
        n_t num;
        cin >> num;
        cout << primes_num[combs_num[num]] << endl;
    }

    return 0;
}
