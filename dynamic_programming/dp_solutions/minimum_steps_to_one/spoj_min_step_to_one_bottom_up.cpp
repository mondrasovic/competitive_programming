#include <vector>
#include <iostream>
#include <algorithm>

static const int kMaxNum = 20000000;

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<size_t> min_count_dp(kMaxNum + 1);
    for (size_t num = 2; num < min_count_dp.size(); ++num) {
        min_count_dp[num] = 1 + min({
            min_count_dp[num - 1],
            (num % 2 == 0) ? min_count_dp[num / 2] : num,
            (num % 3 == 0) ? min_count_dp[num / 3] : num});
    }

    int n_cases;
    cin >> n_cases;

    for (int i = 1; i <= n_cases; ++i) {
        int num;
        cin >> num;
        cout << "Case " << i << ": " << min_count_dp[num] << endl;
    }

    return 0;
}
