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

struct pt {
    double x, y;
    bool operator == (pt const& t) const {
        return x == t.x && y == t.y;
    }
};

vector<pt> Shape(int n) {
    vector<pt> s;
    double N = double(n);
    for(int k = 1; k <= n; k++) {
        double K = double(k);
        s.push_back({
            cos(((2.0 * K - 1.0) / N * 180.0) / (180.0) * M_PI),
            sin(((2.0 * K - 1.0) / N * 180.0) / (180.0) * M_PI),
        });
    }
    return s;
}

int orientation(pt a, pt b, pt c) {
    double v = a.x*(b.y-c.y) + b.x*(c.y-a.y) + c.x*(a.y-b.y);
    if (v < 0) return -1;
    if (v > 0) return +1;
    return 0;
}

bool cw(pt a, pt b, pt c, bool include_collinear) {
    int o = orientation(a, b, c);
    return o < 0 || (include_collinear && o == 0);
}

bool collinear(pt a, pt b, pt c) {
    return orientation(a, b, c) == 0;
}

void convex_hull(vector<pt>& a, bool include_collinear = false) {
    pt p0 = *min_element(a.begin(), a.end(), [](pt a, pt b) {
        return make_pair(a.y, a.x) < make_pair(b.y, b.x);
    });
    sort(a.begin(), a.end(), [&p0](const pt& a, const pt& b) {
        int o = orientation(p0, a, b);
        if (o == 0)
            return (p0.x-a.x)*(p0.x-a.x)+(p0.y-a.y)*(p0.y-a.y)
                 < (p0.x-b.x)*(p0.x-b.x)+(p0.y-b.y)*(p0.y-b.y);
        return o < 0;
    });
    if (include_collinear) {
        int i = (int)a.size() - 1;
        while (i >= 0 && collinear(p0, a[i], a.back())) i--;
        reverse(a.begin()+i+1, a.end());
    }

    vector<pt> st;
    for (int i = 0; i < (int)a.size(); i++) {
        while (st.size() > 1 && !cw(st[st.size()-2], st.back(), a[i], include_collinear))
            st.pop_back();
        st.push_back(a[i]);
    }

    if (!include_collinear && st.size() == 2 && st[0] == st[1])
        st.pop_back();

    a = st;
}

vector<pt> compute_convex_hull(const vector<pair<double, double>>& input, bool include_collinear = false) {
    vector<pt> points;
    for (const auto& p : input)
        points.push_back({p.first, p.second});
    convex_hull(points, include_collinear);
    return points;
}

vector<pt> compute_convex_hull(const vector<pt>& input, bool include_collinear = false) {
    vector<pt> points = input;
    convex_hull(points, include_collinear);
    return points;
}

// int main() {
//     vector<pt> base = {{0.0, 0.0}};
//     for(int sides = 3; sides <= 4; sides++) {
//         cout << "Computing " << sides << endl;
//         // Overlap
//         auto cshape = Shape(sides);
//         int bsz = base.size();
//         for(int i = 0; i < bsz; i++) {
//             for(auto &c : cshape) {
//                 base.push_back({base[i].x + c.x, base[i].y + c.y});
//             }
//         }
//         base = compute_convex_hull(base);
//         cout << "Done adding " << base.size() << endl;
//     }
//     cout << base.size() << endl;
    
// }

map<int, int> pfcs(int n) {
    map<int, int> a;
    for(int q = 2; q <= n; q++) {
        while (n % q == 0) {
            a[q] += 1;
            n /= q;
        }
    }
    return a;
}

int main() {
    vector<pt> base = {{0.0, 0.0}};
    map<int, int> mpc;
    for(int sides = 1864; sides <= 1864; sides++) {
        auto pfs = pfcs(sides);
        for(auto [a, b] : pfs) {
            mpc[a] = max(mpc[a], b);
        }
    }
    int sides = 0;
    for(auto e : mpc) {
        sides += pow(e.first, e.second) - 1;
    }
    cout << sides + 1 << endl;
    
}