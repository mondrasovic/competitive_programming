#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

typedef double n_t;

static const n_t kPi = acos(-1);
static const n_t kEps = 1.e-5;


int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
#endif

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    n_t a_1, b_1, t1, a_2, b_2, t;
    int n_case = 0;
    while ((cin >> a_1 >> b_1 >> t1 >> a_2 >> b_2 >> t) && (a_1 > 0)) {
        auto t_2 = t1 * pow(a_2 / a_1, 1.5);
        t = fmod(t, t_2);

        auto  c_2 = sqrt(a_2 * a_2 - b_2 * b_2);
        auto target_area = kPi * a_2 * b_2 * (t / t_2);
        n_t theta_lower = 0, theta_upper = 2 * kPi;

        for (int i = 0; i < 1000; ++i) {
            auto theta = (theta_lower + theta_upper) / 2;
            auto area = (theta * a_2 * b_2 / 2) - (b_2 * c_2 * sin(theta) / 2);

            if (area < target_area)
                theta_lower = theta;
            else
                theta_upper = theta;
        }

        auto x = a_2 * cos(theta_lower);
        auto y = b_2 * sin(theta_lower);

        cout << "Solar System " << (++n_case) << ": "
            << fixed << setprecision(3) << x << ' ' << y << endl;
    }

    return 0;
}
