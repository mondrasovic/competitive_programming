#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

typedef unsigned long long int n_t;

static vector<n_t> primes_;
static const size_t kMaxNum = 1 << 16; // 2^16 since the input is at most 2^31.

static void init_primes()
{
    vector<bool> is_prime(kMaxNum + 1, true);

    for (size_t i = 2; i < is_prime.size(); ++i) {
        if (is_prime[i]) {
            primes_.emplace_back(i);

            for (size_t j = i * i; j < is_prime.size(); j += i)
                is_prime[j] = false;
        }
    }
}

static int count_div_occurr(n_t num, n_t div, int *count) 
{
    *count = 0;

    while (num % div == 0) {
        num /= div;
        ++(*count);
    }

    return num;
}

static int calc_prime_occurr_in_fact(n_t fact, n_t prime)
{
    auto count = 0;

    for (n_t div = prime; div <= fact; div *= prime)
        count += fact / div;
    
    return count;
}

static bool check_fact_div(n_t n, n_t m)
{
    for (const auto& prime : primes_) {
        if (prime > m)
            break;
        
        int div_count;
        m = count_div_occurr(m, prime, &div_count);
        if (div_count > 0) {
            auto prime_occurr_count = calc_prime_occurr_in_fact(n, prime);
            if (div_count > prime_occurr_count)
                return false;
        }
    }

    return (m <= 1) || (m <= n);
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    init_primes();

    int n, m;

    while (cin >> n >> m) {
        cout << m;
        if (check_fact_div(n, m)) {
            cout << " divides ";
        } else {
            cout << " does not divide ";
        }
        cout << n << '!' << endl;
    }

    return 0;
}
