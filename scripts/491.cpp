#include <bits/stdc++.h>
using namespace std;
using ll = long long;

const ll m_dc = 59049; // 3^10
ll dp[21][11][m_dc];

int main() {
    memset(dp, 0, sizeof(dp));
    dp[0][0][0] = 1;
    for(ll d = 0; d < 20; d++) {
        for(ll carry = 0; carry <= 10; carry++) {
            for(ll dused = 0; dused < m_dc; dused++) {
                if (d <= 2 && dp[d][carry][dused]) {
                    cout << d << ' '<< carry << ' ' << dused << ' ' << dp[d][carry][dused] << endl; 
                }
                // At current, add a new digit. Use the carry and update dused accordingly.
                for(ll d_a = 0; d_a < 10; d_a++) {
                    // Can add
                    ll n_c = (carry + 11 * d_a) / 10;
                    ll n_d = (carry + 11 * d_a) % 10;
                    ll c_dc_m = pow(3, n_d);
                    ll c_dc = ll(dused / c_dc_m) % 3;
                    ll new_dused = dused + c_dc_m;
                    if (c_dc < 2) {
                        dp[d + 1][n_c][new_dused] += dp[d][carry][dused];
                    }
                }
            }
        }
    }
    ll tot = 0;
    for(int i = 1; i < 10; i++) {
        tot += dp[19][i][(m_dc - 1) - int(pow(3, i))];
    }
    cout << tot << endl;
    return 0;
}