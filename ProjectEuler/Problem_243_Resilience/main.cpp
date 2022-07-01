#include <iostream>

using namespace std;

#define N_NUMS 900000000

typedef long double n_t;

static const n_t kTargetRatio(15499.0L / 94744.0L);

static int *init_totient_table()
{
    int *totient = new int[N_NUMS];

    for (register int i = 0; i < N_NUMS; ++i)
    {
        totient[i] = i;
    }

    for (register int i = 2; i < N_NUMS; ++i)
    {
        if (totient[i] == i)
        {
            for (register int j = i; j < N_NUMS; j += i)
            {
                totient[j] -= totient[j] / i;
            }
        }
    }

    return totient;
}

int main()
{
    int *totient = init_totient_table();

    for (register int denom = 2; denom < N_NUMS; ++denom)
    {
        auto resilience(static_cast<n_t>(totient[denom]) / (denom - 1));

        if (resilience < kTargetRatio)
        {
            cout << "Solution: " << denom << endl;
            break;
        }
    }

    delete[] totient;

    return 0;
}
