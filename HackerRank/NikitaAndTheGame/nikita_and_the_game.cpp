#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

typedef unsigned long long int n_t;

static const int kMaxVals = 16384; // 2^14

static int g_n_vals;
static vector<n_t> g_vals(kMaxVals);
static vector<n_t> g_sums(kMaxVals + 1);

static int calc_max_score(size_t i, size_t j)
{
    auto segm_sum = g_sums[j + 1] - g_sums[i];
    if (segm_sum == 0) {
        return j - i;
    }
    if ((segm_sum & 1) || (j - i == 0)) {
        return 0;
    }

    auto segm_sum_half_plus_shift((segm_sum >> 1) + g_sums[i]);

    const auto& g_sums_begin_it(g_sums.begin());
    const auto& segm_it_begin(g_sums_begin_it + i + 1);
    const auto& segm_it_end(g_sums_begin_it + j + 2);

    auto half_sum_it(lower_bound(segm_it_begin, segm_it_end, segm_sum_half_plus_shift));
    
    auto score = 0;
    if ((half_sum_it != segm_it_end) && (*half_sum_it == segm_sum_half_plus_shift)) {
        auto k = distance(segm_it_begin, half_sum_it) + i;
        score = max(score, 1 + max(calc_max_score(i, k), calc_max_score(k + 1, j)));
    }

    return score;
}

int main()
{
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
        cout << calc_max_score(0, g_n_vals - 1) << endl;
    }

    return 0;
}
