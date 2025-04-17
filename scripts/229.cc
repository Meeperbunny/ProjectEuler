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

const int N = 2e9;

int main() {
    vector<ll> constmod = {1, 2, 3, 7};
    vector<bitset<N + 1>> bitsets(constmod.size());
    for(int k = 0; k < constmod.size(); k++) {
        for(ll i = 1; i * i < N; i++) {
            for(ll q = 1;; q++) {
                ll num = i * i + q * q * constmod[k];
                if (num > N) break;
                bitsets[k][num] = 1;
            }
        }
    }
    ll cnt = 0;
    for(ll i = 1; i <= N; i++) {
        if (bitsets[0][i] & bitsets[1][i] & bitsets[2][i] & bitsets[3][i]) {
            cnt += 1;
        }
    }
    cout << cnt << endl;
    return 0;
}