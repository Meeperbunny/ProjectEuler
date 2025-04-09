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
from heapq import *
from tqdm import trange
N = 10**9
min_cost = [0]
for i in trange(1, N):
    # Get min cost
    mc = heappop(min_cost)
    heappush(min_cost, mc + 1)
    heappush(min_cost, mc + 4)
len(min_cost), sum(min_cost)
*/

int main() {
    priority_queue<ll, vector<ll>, greater<ll>> Q;
    Q.push(0);
    int N = 1e9;
    for(int i = 1; i < N; i++) {
        ll c = Q.top();
        Q.pop();
        Q.push(c + 1);
        Q.push(c + 4);
    }
    ll t = 0;
    while(Q.size()) {
        t += Q.top();
        Q.pop();
    }
    cout << t << endl;
    return 0;
}