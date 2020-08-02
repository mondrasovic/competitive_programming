#include <stdio.h>

#define MOD 1000000007
#define SIZE 1001

typedef long long int n_t;

static n_t row_combs[SIZE] = {[0] = 1, [1] = 1, [2] = 2, [3] = 4};
static n_t all_walls[SIZE][SIZE];
static n_t solid_walls[SIZE][SIZE];

int main()
{
    for (int i = 4; i < SIZE; ++i) {
        row_combs[i] = (row_combs[i - 1] +
            row_combs[i - 2] +
            row_combs[i - 3] +
            row_combs[i - 4]) % MOD;
    }

    for (int j = 0; j < SIZE; ++j) {
        n_t combs = row_combs[j];

        all_walls[0][j] = 1;
        for (int i = 1; i < SIZE; ++i) {
            n_t coef = combs * (i % 2 == 1) + 1 * (i % 2 == 0);
            n_t sub_res = all_walls[i / 2][j];
            all_walls[i][j] = (((sub_res * sub_res) % MOD) * coef) % MOD;
        }
    }

    for (int i = 0; i < SIZE; ++i) {
        solid_walls[i][0] = solid_walls[i][1] = 1;
        for (int j = 2; j < SIZE; ++j) {
            n_t invalid_walls = 0;
            for (int k = 1; k < j; ++k) {
                invalid_walls = (invalid_walls +
                    (solid_walls[i][k] *
                    all_walls[i][j - k]) % MOD) % MOD;
            }
            solid_walls[i][j] = (all_walls[i][j] - invalid_walls + MOD) % MOD;
        }
    }

    int n_cases;
    scanf("%d", &n_cases);

    while (--n_cases >= 0) {
        int height, width;
        scanf("%d %d", &height, &width);
        printf("%lld\n", solid_walls[height][width]);
    }

    return 0;
}
