#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

static const int kValidVal = 0;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    size_t n_rows, n_cols;
    while ((cin >> n_rows >> n_cols) && (n_rows > 0)) {
        vector<vector<int>> row_max_segm_len(n_rows, vector<int>(n_cols));

        for (size_t i = 0; i < n_rows; ++i) {
            for (size_t j = 0; j < n_cols; ++j) {
                int curr_val;

                if ((cin >> curr_val) && (curr_val == kValidVal)) {
                    row_max_segm_len[i][j] = ((j == 0) ? 0 : row_max_segm_len[i][j - 1]) + 1;
                }
            }
        }

        int res_max_rect_area = 0;

        for (size_t i = 0; i < n_rows; ++i) {
            for (size_t j = 0; j < n_cols; ++j) {
                if (row_max_segm_len[i][j] == 0) {
                    continue;
                }

                auto rect_width = row_max_segm_len[i][j];
                int curr_area = rect_width;

                for (int k = i - 1; (k >= 0) && (row_max_segm_len[k][j] >= rect_width); --k) {
                    curr_area += rect_width;
                }

                for (size_t k = i + 1; (k < n_rows) && (row_max_segm_len[k][j] >= rect_width); ++k) {
                    curr_area += rect_width;
                }

                res_max_rect_area = max(res_max_rect_area, curr_area);
            }
        }

        cout << res_max_rect_area << endl;
    }

    return 0;
}
