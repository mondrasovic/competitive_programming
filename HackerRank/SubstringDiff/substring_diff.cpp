#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

static bool check_substr_exists(
    const vector<vector<int>>& mismatches_count,
    size_t str_len, int max_diffs_num)
{
    for (auto i = str_len; i < mismatches_count.size(); ++i) {
        for (auto j = str_len; j < mismatches_count[i].size(); ++j) {
            auto diffs_num = mismatches_count[i][j] -
                mismatches_count[i - str_len][j - str_len];
            if (diffs_num <= max_diffs_num) {
                return true;
            }
        }
    }

    return false;
}

static size_t max_k_diffs_substring_len(
    const string& str_1,
    const string& str_2,
    int max_diffs_num)
{
    vector<vector<int>> mismatches_count(
        str_1.size() + 1, vector<int>(str_2.size() + 1, 0));
    
    for (size_t i = 1; i < mismatches_count.size(); ++i) {
        for (size_t j = 1; j < mismatches_count[i].size(); ++j) {
            mismatches_count[i][j] = mismatches_count[i - 1][j - 1] +
                (1 * (str_1[i - 1] != str_2[j - 1]));
        }
    }

    size_t max_valid_len = 0;
    size_t lower = 0;
    size_t higher = str_1.size();

    while (lower < higher) {
        auto mid = (lower + higher + 1) >> 1;
        if (check_substr_exists(mismatches_count, mid, max_diffs_num)) {
            max_valid_len = max(max_valid_len, mid);
            lower = mid;
        } else {
            higher = mid - 1;
        }
    }

    return max_valid_len;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int cases_num;
    cin >> cases_num;

    while (cases_num-- > 0) {
        int max_diffs_num;
        string str_1, str_2;
        cin >> max_diffs_num >> str_1 >> str_2;
        cout << max_k_diffs_substring_len(str_1, str_2, max_diffs_num) << endl;
    }

    return 0;
}
