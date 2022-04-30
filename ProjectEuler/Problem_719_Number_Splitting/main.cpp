#include <cmath>
#include <iostream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef long long int n_t;

static const n_t kMaxNum = 1000000000000;

bool is_num_split_sum_reachable(n_t num, n_t sum)
{
    if (num < 10)
    {
        return num == sum;
    }

    if (num < sum)
    {
        return false;
    }
    else if (num == sum)
    {
        return true;
    }

    n_t div = 1;
    for (int i = 0; i < static_cast<int>(log10l(num)); ++i)
    {
        div *= 10;
    }

    while (div > 0)
    {
        auto head = num / div;
        auto tail = num % div;
        if (is_num_split_sum_reachable(tail, sum - head))
        {
            return true;
        }
        div = div / 10;
    }

    return false;
}

int main()
{
    n_t target_sum = 0;
    n_t num = 2;

    while (true)
    {
        auto square = num * num;
        if (square > kMaxNum)
        {
            break;
        }

        if (is_num_split_sum_reachable(square, num) > 0)
        {
            target_sum += square;
        }

        ++num;
    }

    cout << "Solution: " << target_sum << endl;

    return 0;
}
