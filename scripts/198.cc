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

ll gcd(ll a, ll b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

using Fraction = pair<ll, ll>;

void simplify(Fraction& f) {
    ll g = gcd(f.first, f.second);
    f.first /= g;
    f.second /= g;
}

Fraction add(const Fraction &a, const Fraction &b) {
    Fraction added = {a.first * b.second + b.first * a.second, a.second * b.second};
    simplify(added);
    return added;
}

Fraction mean(const Fraction &a, const Fraction &b) {
    Fraction added = {a.first * b.second + b.first * a.second, a.second * b.second * 2ll};
    simplify(added);
    return added;
}

Fraction pseudoMean(const Fraction &a, const Fraction &b) {
    Fraction added = {a.first + b.first, a.second + b.second};
    simplify(added);
    return added;
}

struct PairHash {
    std::size_t operator()(const std::pair<long long, long long>& p) const {
        return std::hash<long long>()(p.first) ^ (std::hash<long long>()(p.second) << 1);
    }
};
    
unordered_set<pair<ll, ll>, PairHash> S;

void traverse(ll D, Fraction L, Fraction M, Fraction R) {
    Fraction lm = pseudoMean(L, M);
    Fraction rm = pseudoMean(M, R);

    Fraction l_mean = mean(M, lm);
    Fraction r_mean = mean(M, rm);
    
    if (l_mean.second <= D)
        S.insert(l_mean);
    if (r_mean.second <= D)
        S.insert(r_mean);
    if (M.second * M.second > D) {
        return;
    }

    traverse(D, L, lm, M);
    traverse(D, M, rm, R);
}

int main() {
    ll D = 10'000'000;
    Fraction L = {0, 1};
    Fraction M = {1, 101};
    Fraction R = {1, 100};
    traverse(D, L, M, R);
    cout << S.size() << endl;
}