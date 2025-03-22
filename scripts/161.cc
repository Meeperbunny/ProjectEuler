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


/*
** ... ... ...
** [2] [b] ...
** [1] [a] ...
** [0] [9] ...
*/

int main() {
    const ll C = 12, R = 9;
    unordered_map<ll, ll> masks;
    masks.insert({0, 1});
    for(ll c = 0; c < C; c++) {
        for(ll r = 0; r < R; r++) {
            unordered_map<ll, ll> nextMasks;
            ll bitToCheck = (1 << r);
            for(auto &[m, cnt] : masks) {
                if (m & bitToCheck) {
                    nextMasks[m] += cnt;
                }
                else {
                    vector<ll> P;
                    if (r + 3 <= R) {
                        P.push_back((1 << (r + 0)) | (1 << (r + 1)) | (1 << (r + 2)));
                    }
                    if (r + 2 <= R) {
                        P.push_back((1 << (r + 0)) | (1 << (r + 1)) | (1 << (r + 10)));
                        P.push_back((1 << (r + 0)) | (1 << (r + 9)) | (1 << (r + 10)));
                        P.push_back((1 << (r + 1)) | (1 << (r + 0)) | (1 << (r + 9)));
                    }
                    if (r + 1 <= R) {
                        P.push_back((1 << (r + 0)) | (1 << (r + 9)) | (1 << (r + 18)));
                        if (r > 0) {
                            P.push_back((1 << (r + 0)) | (1 << (r + 9)) | (1 << (r + 8)));
                        }
                    }
                    for(auto p : P) {
                        if ((p + m) == (p ^ m)) {
                            nextMasks[p | m] += cnt;
                        }
                    }
                }
            }
            swap(masks, nextMasks);
        }
        unordered_map<ll, ll> shifted;
        ll cmask = (1 << 9) - 1;
        for(auto &[m, cnt] : masks) {
            assert((m & cmask) == cmask);
            shifted[m >> 9] += cnt;
        }
        if (c == C - 1) {
            cout << masks[cmask] << endl;
            return 0;
        }
        swap(masks, shifted);
    }
    return 0;
}