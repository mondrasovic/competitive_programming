#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <functional>

using namespace std;

static vector<int> vals_;

static void print_used_vals(int used_vals)
{
    string sep("");

    for (size_t i = 0; i < vals_.size(); ++i) {
        auto bit_flag = 1 << i;

        if (used_vals & bit_flag) {
            cout << sep << vals_[i];
            sep = '+';
        }
    }
    cout << endl;
}

static bool find_sums(int rem_sum, unsigned used_vals = 0, size_t pos = 0)
{
    if (rem_sum < 0) {
        return false;
    } else if (rem_sum == 0) {
        print_used_vals(used_vals);
        return true;
    } else {
        auto ret = false;
        auto n_vals = vals_.size();

        if (pos < n_vals) {
            auto next_pos = pos + 1;
            ret |= find_sums(
                rem_sum - vals_[pos], used_vals | (1 << pos), next_pos);
            
            while ((next_pos < n_vals) && (vals_[next_pos] == vals_[pos]))
                ++next_pos;
            
            if (next_pos < n_vals)
                ret |= find_sums(rem_sum, used_vals, next_pos);
        }

        return ret;
    }
}

int main()
{
    //freopen("input.txt", "rt", stdin);
    //freopen("output.txt", "wt", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int target_sum, n_vals;

    while ((cin >> target_sum >> n_vals) && (n_vals > 0)) {
        vals_.clear();
        for (int i = 0; i < n_vals; ++i) {
            int val;
            cin >> val;
            vals_.emplace_back(val);
        }
        sort(vals_.begin(), vals_.end(), greater<int>());

        cout << "Sums of " << target_sum << ':' << endl;
        if (!find_sums(target_sum)) {
            cout << "NONE" << endl;
        }
    }

    return 0;
}
