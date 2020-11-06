#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n_cases;
    cin >> n_cases;

    while (--n_cases >= 0) {
        int grid_size, n_blocks;
        cin >> grid_size >> n_blocks;

        vector<vector<bool>> grid(grid_size, vector<bool>(grid_size, true));

        while (--n_blocks >= 0) {
            int row_1, col_1, row_2, col_2;
            cin >> row_1 >> col_1 >> row_2 >> col_2;

            for (int i = row_1 - 1; i < row_2; ++i) {
                for (int j = col_1 - 1; j < col_2; ++j) {
                    grid[i][j] = false;
                }
            }
        }

        vector<vector<int>> max_row_segm_len(grid_size, vector<int>(grid_size));

        for (int i = 0; i < grid_size; ++i) {
            for (int j = 0; j < grid_size; ++j) {
                if (grid[i][j]) {
                    max_row_segm_len[i][j] = ((j == 0) ? 0 : max_row_segm_len[i][j - 1]) + 1;
                }
            }
        }

        int max_rect_area = 0;

        for (int i = 0; i < grid_size; ++i) {
            for (int j = 0; j < grid_size; ++j) {
                auto curr_width = max_row_segm_len[i][j];
                auto curr_area = curr_width;

                for (int k = i - 1; (k >= 0) && (max_row_segm_len[k][j] >= curr_width); --k) {
                    curr_area += curr_width;
                }

                for (int k = i + 1; (k < grid_size) && (max_row_segm_len[k][j] >= curr_width); ++k) {
                    curr_area += curr_width;
                }

                max_rect_area = max(max_rect_area, curr_area);
            }
        }

        cout << max_rect_area << endl;
    }

    return 0;
}
