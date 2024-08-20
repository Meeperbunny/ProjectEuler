#include <bits/stdc++.h>
using namespace std;
#define HEADER ios::sync_with_stdio(0);cin.tie(0);if (fopen("file.in", "r")) {freopen("file.in", "r+", stdin);};
#define all(v) v.begin(), v.end()
using ll = long long;
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }

#ifdef IAN_DEBUG
#define dbg(...) cerr << '[' << __FILE__ << ':' << __LINE__ << "] (" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

ll dp[31][4][4][4][81];

void TC() {
    memset(dp, 0, sizeof(dp));
    dp[0][0][0][0][0] = 1;
    for(int i = 1; i <= 30; i++) {
        for(int c1 = 0; c1 < 4; c1++) {
            for(int c2 = 0; c2 < 4; c2++) {
                for(int c3 = 0; c3 < 4; c3++) {
                    for(int c4 = 0; c4 < 4; c4++) {
                        bool free = false, fare = false, area = false, reef = false;
                        if (i >= 4 && c1 == 2 && c2 == 3 && c3 == 1 && c4 == 1) free = true;
                        if (i >= 4 && c1 == 2 && c2 == 0 && c3 == 3 && c4 == 1) fare = true;
                        if (i >= 4 && c1 == 0 && c2 == 3 && c3 == 1 && c4 == 0) area = true;
                        if (i >= 4 && c1 == 3 && c2 == 1 && c3 == 1 && c4 == 2) reef = true;
                        // assert(int(free) + int(fare) + int(area) + int(reef) <= 1);
                        for(int c = 0; c < 81; c++) {
                            int free_c = min(2, c % 3 + int(free));
                            int fare_c = min(2, (c / 3) % 3 + int(fare));
                            int area_c = min(2, (c / 9) % 3 + int(area));
                            int reef_c = min(2, (c / 27) % 3 + int(reef));
                            dp[i][c2][c3][c4][free_c + fare_c * 3 + area_c * 9 + reef_c * 27] += dp[i - 1][c1][c2][c3][c];
                        }
                            
                    }
                }
            }
        }
    }
    ll tot = 0;
    ll total = 0;
    for(int i = 0; i < 4; i++) {
        for(int q = 0; q < 4; q++) {
            for(int j = 0; j < 4; j++) {
                tot += dp[30][i][q][j][1 + 3 + 9 + 27];
            }
        }
    }
    cout << tot << endl;
}

int main() {
    HEADER;
    int T = 1;
    // cin >> T;
    for (int t = 0; t < T; t++) {
        TC();
    }
    return 0;
}