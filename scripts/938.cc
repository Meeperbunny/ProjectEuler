#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

int main() {
    const int N = 24690;
    const int M = 12345;
    
    vector<vector<double>> prob(N + 1, vector<double>(M + 1, 0.0));
    prob[N][M] = 1.0;
    
    for (int n = N; n >= 0; n--) {
        for (int m = M; m >= 0; m--) {
            int t = n + m;
            if (n == 0 || m == 0)
                continue;
            if (t <= 1)
                continue;
            double p_first_red   = static_cast<double>(n) / t;
            double p_second_red  = static_cast<double>(n - 1) / (t - 1);
            double p_first_black = static_cast<double>(m) / t;
            double p_second_black = static_cast<double>(m - 1) / (t - 1);
            double p_both_red   = p_first_red * p_second_red;
            double p_both_black = p_first_black * p_second_black;
            double p_other = 1.0 - (p_both_red + p_both_black);
            double total = p_both_red + p_other;
            double p_remove_two_reds = p_both_red / total;
            double p_remove_one_black = p_other / total;
            if (n >= 2) {
                prob[n - 2][m] += prob[n][m] * p_remove_two_reds;
            }
            if (m >= 1) {
                prob[n][m - 1] += prob[n][m] * p_remove_one_black;
            }
        }
    }
    
    double T = 0.0;
    cout << fixed << setprecision(20);
    for (int i = 1; i < M; i++) {
        T += prob[0][i];
    }
    cout << "T = " << T << "\n";
    
    return 0;
}
