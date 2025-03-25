#include <bits/stdc++.h>
using namespace std;
#define HEADER ios::sync_with_stdio(0);cin.tie(0);if (fopen("file.in", "r")) {freopen("file.in", "r+", stdin);};
#define all(v) v.begin(), v.end()
using ll = unsigned long long;
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }

#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#ifdef IAN_DEBUG
#define dbg(...) cerr << '[' << __FILE__ << ':' << __LINE__ << "] (" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

ll B(ll k) {
    return __builtin_popcount(k);
}

ll U(ll n) {
    return pow(2, B(3 * n)) + pow(3, B(2 * n)) + B(n + 1);
}

ll getArea(double a, double b, double c, double d) {
    double s = (a + b + c + d) / 2;
    return sqrt((s - a) * (s - b) * (s - c) * (s - d));
}

int main() {
    multiset<ll> maxes;
    for(int i = 1; i <= 10; i++) {
        cout << U(i) << ' ';
    } cout << endl;
    const ll N = 3'000'000;
    ll ans = 0;
    for(int i = 1; i <= N; i++) {
        ll u = U(i);
        maxes.insert(u);
        if (i < 4) continue;
        double bestArea = 0;
        ll bestPer = 0;

        vector<ll> sides(4);
        auto it = maxes.rbegin();
        for(int q = 0; q < 4; q++) {
            sides[q] = *it++;
        }
        double A = getArea(sides[0], sides[1], sides[2], sides[3]);
        if (A > bestArea) {
            bestArea = A;
            bestPer = accumulate(all(sides), 0ll);
        }
        for(int q = 0; it != maxes.rend() && q < 300; q++) {
            sides[q % 4] = *it++;
            double A = getArea(sides[0], sides[1], sides[2], sides[3]);
            if (A > bestArea) {
                bestArea = A;
                bestPer = accumulate(all(sides), 0ll);
            }
        }
        ans += bestPer;
        if (i == 5 || i == 10 || i == 150) {
            cout << bestArea << ' ' << bestPer << endl;
        }
    }
    cout << ans << endl;
    return 0;
}