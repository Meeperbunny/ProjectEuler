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

void pmask(ll m) {
    cout << "Mask: " << m << endl;
    for(ll q = 8; q >= 0; q--) {
        for(ll i = 0; i < 4; i++) {
            cout << ((m >> (q + i * 9)) & 1);
        } cout << endl;
    }
}

int main() {
    const ll C = 12, R = 9;
    unordered_map<ll, ll> masks;
    masks.insert({0, 1});
    for(ll c = 0; c < C; c++) {
        cout << c << ' ' << masks.size() << endl;
        for(ll r = 0; r < R; r++) {
            unordered_map<ll, ll> nextMasks;
            ll bitToCheck = (1 << r);
            for(auto &[m, cnt] : masks) {
                // if (c == 0 && r == 2) {
                //     cout << "c = " << c << ", r = " << r << ": cnt = " << cnt << endl;
                //     pmask(m);
                // }
                // If current mask is good, then pass onto next.
                // If current is not good, fill and pass onto next.
                if (m & bitToCheck) {
                    // Is good, pass onto next
                    nextMasks[m] += cnt;
                }
                else {
                    // Is not good. Fill.
                    vector<ll> P;
                    if (r + 3 <= R) {
                        // U bar
                        P.push_back((1 << (r + 0)) | (1 << (r + 1)) | (1 << (r + 2)));
                    }
                    if (r + 2 <= R) {
                        // UR bar
                        P.push_back((1 << (r + 0)) | (1 << (r + 1)) | (1 << (r + 10)));
                        // RU bar
                        P.push_back((1 << (r + 0)) | (1 << (r + 9)) | (1 << (r + 10)));
                        // DR bar
                        P.push_back((1 << (r + 1)) | (1 << (r + 0)) | (1 << (r + 9)));
                    }
                    if (r + 1 <= R) {
                        // R bar
                        P.push_back((1 << (r + 0)) | (1 << (r + 9)) | (1 << (r + 18)));
                        if (r > 0) {
                            // RD bar
                            P.push_back((1 << (r + 0)) | (1 << (r + 9)) | (1 << (r + 8)));
                        }
                    }
                    // For each piece mask, if can fit current piece insert the current, then add it
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
        // If at the end of the row, move all to the left 1
        // cout << "MSIZE " << masks.size() << endl;
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