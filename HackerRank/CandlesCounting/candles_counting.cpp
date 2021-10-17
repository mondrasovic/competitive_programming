#include <iostream>
#include <vector>
#include <map>
#include <set>

using namespace std;

typedef unsigned long long int n_t;

static const n_t kMod = 1000000007;

static n_t count_colorful_subseqs(const vector<int>& heights, const vector<int>& colors, int n_colors)
{
    auto n_color_subsets(1 << n_colors);
    n_t max_count = 0;
    
    return max_count;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n_candles, n_colors;
    cin >> n_candles >> n_colors;

    vector<int> heights(n_candles);
    vector<int> colors(n_candles);

    for (int i = 0; i < n_candles; ++i) {
        int color;
        cin >> heights[i] >> color;
        colors[i] = color - 1;
    }

    cout << count_colorful_subseqs(heights, colors, n_colors) << endl;

    return 0;
}
