#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

static const int kMaxVals = 16384; // 2^14

static int g_n_vals;
static vector<int> g_vals(kMaxVals);
static vector<int> g_sums(kMaxVals + 1);

static int calc_max_score(size_t i, size_t j)
{
    auto segm_sum = g_sums[j + 1] - g_sums[i];
    if (segm_sum == 0) {
        return j - i;
    }
    if (segm_sum & 1) {
        return 0;
    }

    auto segm_sum_half(segm_sum >> 1);
    cout << "segment sum: " << segm_sum_half << endl;
    auto segm_it_end(g_vals.begin() + j + 1);
    auto half_sum_it(
        lower_bound(g_vals.begin() + i, segm_it_end, segm_sum_half));
    cout << "sum: " << *half_sum_it << endl;
    cout << "position: " << half_sum_it - g_vals.begin() << endl;
    auto score = 0;
    auto k = i;
    while ((half_sum_it != segm_it_end) && (*half_sum_it == segm_sum_half)) {
        cout << "found..." << endl;
        score = max(
            score,
            1 + max(calc_max_score(i, k), calc_max_score(k + 1, j)));
        ++half_sum_it, ++k;
    }

    /*for (size_t k = i; k < j; ++k) {
        auto sum_left(g_sums[k + 1] - g_sums[i]);
        auto sum_right(g_sums[j + 1] - g_sums[k + 1]);
        if (sum_left == sum_right) {
            score = max(
                score,
                1 + max(calc_max_score(i, k), calc_max_score(k + 1, j)));
        }
    }*/

    return score;
}

int main()
{
    /*vector<int> vals{1, 2, 3, 4, 4, 5, 6};
    cout << *lower_bound(vals.begin(), vals.end(), 0);*/

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n_cases;
    cin >> n_cases;

    while (--n_cases >= 0) {
        cin >> g_n_vals;
        for (int i = 0; i < g_n_vals; ++i) {
            cin >> g_vals[i];
        }

        g_sums[0] = 0;
        for (int i = 0; i < g_n_vals; ++i) {
            g_sums[i + 1] = g_sums[i] + g_vals[i];
        }
        cout << "test case" << endl;
        cout << calc_max_score(0, g_n_vals - 1) << endl;
    }

    return 0;
}
