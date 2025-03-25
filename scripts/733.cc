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

ll M = 1e9+7;
class FenwickTree {
public:
    int n;
    vector<ll> fenw;
    FenwickTree(int n): n(n), fenw(n+1, 0) {}
    void update(int i, ll delta) {
        for(; i <= n; i += i & -i)
            fenw[i] += delta;
    }
    ll query(int i) {
        ll sum = 0;
        for(; i; i -= i & -i) {
            sum += fenw[i];
            sum %= M;
        }
        return sum;
    }
    ll rangeQuery(int l, int r) {
        return (query(r) - query(l - 1) + M) % M;
    }
};

int main() {
    const ll a = 153;
    ll b = a;
    const ll mod = 10000019;
    const ll N = 1000000;
    vector<ll> S;
    for(int i = 0; i < N; i++) {
        S.push_back(b);
        b = (b * a) % mod;
    }
    // for(auto e : S) cout << e<< ' ';
    // cout << endl;
    vector<ll> cp(S);
    sort(all(cp));
    unordered_map<ll, ll> indMap;
    for(int i = 0; i < N; i++) {
        indMap[cp[i]] = i + 1;
    }
    vector<FenwickTree> sumTrees = vector<FenwickTree>(4, FenwickTree(N));
    vector<FenwickTree> cntTrees = vector<FenwickTree>(4, FenwickTree(N));
    for(int i = 0; i < N; i++) {
        ll el = S[i];
        ll ind = indMap[el];
        // cout << "###### " << i << " ########" << endl;
        // for(int q = 0; q < 3; q++) {
        //     for(int z = 1; z <= N; z++) {
        //         cout << sumTrees[q].rangeQuery(z, z) << ' ';
        //     } cout << endl;
        // }
        for(int q = 3; q >= 1; q--) {
            ll d = sumTrees[q - 1].rangeQuery(1, ind) % M;
            ll cnt = cntTrees[q - 1].rangeQuery(1, ind) % M;
            ll ta = (d + el * cnt) % M;
            sumTrees[q].update(ind, ta);
            cntTrees[q].update(ind, cnt);
        }
        sumTrees[0].update(ind, el);
        cntTrees[0].update(ind, 1);
    }
    cout << sumTrees[3].rangeQuery(1, N);
    return 0;
}