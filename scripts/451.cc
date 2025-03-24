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

// const ll N = 100;
const ll N = 2e7;


unordered_set<ll> combine(ll n, const vector<ll> &a, const vector<ll> &b) {
    unordered_set<ll> c;
    for(auto &d1 : a) {
        for(auto &d2 : b) {
            if (d1 * d2 <= N)
                c.insert(d1 * d2);
        }
    }
    return c;
}

int main() {
    // Compute divs
    cout << "Computing divs" << endl;
    vector<vector<ll>> divs(N + 2);
    for(ll i = 2; i < N + 2; i++) {
        if (i < 20) cout << i << endl;
        for(ll q = i; q < N + 2; q += i) {
            divs[q].push_back(i);
        }
    }
    cout << "Done!" << endl;
    
    vector<ll> ans(N + 1, 1);
    ll inc = 10000;
    ll nx = 0;
    for(ll n = 3; n <= N; n++) {
        if (n > nx) {
            cout << double(n) / N << endl;
            nx += inc;
        }
        auto &A = divs[n - 1];
        auto &B = divs[n + 1];
        auto divs = combine(n, A, B);
        for(auto &d : divs) {
            if (n < d - 1)
                ans[d] = max(ans[d], n);
        }
    }
    for(auto e : {7, 15, 100}) {
        cout << "ans[" << e << "] = " << ans[e] << endl; 
    }
    cout << accumulate(ans.begin(), ans.end(), 0ll) - 3ll << endl;
    return 0;
}