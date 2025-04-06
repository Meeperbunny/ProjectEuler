#include <bits/stdc++.h>
using namespace std;
#define HEADER ios::sync_with_stdio(0);cin.tie(0);if (fopen("file.in", "r")) {freopen("file.in", "r+", stdin);};
#define all(v) v.begin(), v.end()
using ll = long long;
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#ifdef IAN_DEBUG
#define dbg(...) cerr << '[' << __FILE__ << ':' << __LINE__ << "] (" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

int counts[11001][11001];

vector<ll> S(300000);

int main() {
    ll m = 1000000;
    for(ll k = 1; k <= 300000; k++) {
        ll K = k - 1;
        if (k <= 55) {
            S[K] = (100003 - 200003 * k + 300007 * (k * k * k % m) + m) % m;
        }
        else {
            S[K] = (S[K - 24] + S[K - 55]) % m;
        }
    }
    vector<vector<ll>> updates;
    for(int i = 0; i < 50000; i++) {
        int x = S[6 * i + 0] % 10000;
        int y = S[6 * i + 1] % 10000;
        int z = S[6 * i + 2] % 10000;
        int dx = 1 + (S[6 * i + 3]) % 399;
        int dy = 1 + (S[6 * i + 4]) % 399;
        int dz = 1 + (S[6 * i + 5]) % 399;
        updates.push_back({
            {z, 1, x, x + dx - 1, y, y + dy - 1}
        });
        updates.push_back({
            {z + dz, 0, x, x + dx - 1, y, y + dy - 1}
        });
    }
    sort(all(updates), [](vector<ll> &a, vector<ll> &b){
        return a[0] < b[0];
    });
    ll ac = 0;
    int i = 0;
    ll tc = 0;
    for(int z = -1; z <= 11000; z++) {
        while(i < updates.size() && updates[i][0] <= z) {
            auto &v = updates[i];
            if (v[1] == 1) {
                for(int x = v[2]; x <= v[3]; x++) {
                    for(int y = v[4]; y <= v[5]; y++) {
                        // cout << x << ' ' << y << endl;
                        if (counts[x][y]++ == 0) {
                            ac += 1;
                        }
                    }
                }

            }
            else {
                for(int x = v[2]; x <= v[3]; x++) {
                    for(int y = v[4]; y <= v[5]; y++) {
                        // cout << x << ' ' << y << endl;
                        if (--counts[x][y] == 0) {
                            ac -= 1;
                        }
                    }
                }
            }
            i++;
        }
        tc += ac;
    }
    cout << tc << endl;
    return 0;
}