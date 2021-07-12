#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

static const int kMaxNum = 20000000;

static vector<int> _min_count_memo(kMaxNum + 1, -1);

static int find_min_count(int num)
{
    if (_min_count_memo[num] >= 0) {
        return _min_count_memo[num];
    }

    auto res = 1 + min({
        find_min_count(num - 1),
        (num % 2 == 0) ? find_min_count(num / 2) : num,
        (num % 3 == 0) ? find_min_count(num / 3) : num});

    return _min_count_memo[num] = res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    _min_count_memo[0] = _min_count_memo[1] = 0;

    int n_cases;
    cin >> n_cases;

    for (int i = 1; i <= n_cases; ++i) {
        int num;
        cin >> num;
        cout << "Case " << i << ": " << find_min_count(num) << endl;
    }

    return 0;
}
