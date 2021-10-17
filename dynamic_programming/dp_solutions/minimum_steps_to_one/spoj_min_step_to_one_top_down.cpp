#include <iostream>
#include <algorithm>

using namespace std;

static int find_min_count(int num)
{
    if (num == 1) {
        return 0;
    }

    return 1 + min({
        find_min_count(num - 1),
        (num % 2 == 0) ? find_min_count(num / 2) : num,
        (num % 3 == 0) ? find_min_count(num / 3) : num});
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n_cases;
    cin >> n_cases;

    for (int i = 1; i <= n_cases; ++i) {
        int num;
        cin >> num;
        cout << "Case " << i << ": " << find_min_count(num) << endl;
    }

    return 0;
}
