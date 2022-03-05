#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

static const int kMaxNum = 100000000;

static unsigned long long count_prime_triplet_geo_seqs(int max_num)
{
    vector<unsigned long long> primes;
    auto approx_primes_num = static_cast<int>(max_num / log(max_num));
    primes.reserve(approx_primes_num);

    vector<bool> is_prime(max_num, true);
    is_prime[0] = is_prime[1] = false;

    auto limit = static_cast<size_t>(sqrt(max_num));
    for (size_t i = 2; i < is_prime.size(); ++i)
    {
        if (is_prime[i])
        {
            primes.emplace_back(i);

            if (i <= limit)
            {
                for (size_t j = i * i; j < is_prime.size(); j += i)
                {
                    is_prime[j] = false;
                }
            }
        }
    }

    unsigned long long terms_sum = 0;

    for (size_t i = 0; i < primes.size() - 1; ++i)
    {
        auto a = primes[i];
        auto a_succ = a + 1;

        for (size_t j = i + 1; j < primes.size(); ++j)
        {
            auto b = primes[j];
            auto b_succ = b + 1;

            long double c_succ = (b_succ * b_succ) / static_cast<long double>(a_succ);
            if (c_succ > max_num)
            {
                break;
            }

            if (labs(c_succ - static_cast<unsigned long long>(c_succ)) > 1e-10)
            {
                continue;
            }

            auto c = static_cast<unsigned long long>(roundl(c_succ)) - 1;
            if (is_prime[c])
            {
                // cout << "(" << a << ", " << b << ", " << c << ")" << endl;
                terms_sum += a + b + c;
            }
        }
    }

    return terms_sum;
}

int main()
{
    cout << "S(100) = " << count_prime_triplet_geo_seqs(100) << endl;
    cout << "S(" << kMaxNum << ") = " << count_prime_triplet_geo_seqs(kMaxNum) << endl;

    return 0;
}
