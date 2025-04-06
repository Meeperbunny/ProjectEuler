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

using Pos = tuple<ll, ll, int>;
const double pi = M_PI;

int main() {
    vector<vector<tuple<double, double, int>>> translations(360), rtranslations(360);
    int angle = 90;
    double xdist = 1.0 - cos(2. * pi / 5.);
    double ydist = sin(2. * pi / 5.);
    translations[angle].push_back({xdist, ydist, (angle - 72 + 360) % 360});
    translations[angle].push_back({-xdist, ydist, (angle + 72 + 360) % 360});
    for(int i = 1; i < 5; i++) {
        int lastAngle = angle;
        angle = (angle + 72) % 360;
        // Rotate the translation left 72 degrees.
        for(auto &[x, y, a] : translations[lastAngle]) {
            double newX = x * cos(2 * pi / 5) - y * sin(2 * pi / 5);
            double newY = x * sin(2 * pi / 5) + y * cos(2 * pi / 5);
            translations[angle].push_back({newX, newY, (72 + a) % 360});
        }
    }
    angle = 90;
    rtranslations[angle].push_back({xdist, -ydist, (angle + 72 + 360) % 360});
    rtranslations[angle].push_back({-xdist, -ydist, (angle - 72 + 360) % 360});
    for(int i = 1; i < 5; i++) {
        int lastAngle = angle;
        angle = (angle + 72) % 360;
        // Rotate the translation left 72 degrees.
        for(auto &[x, y, a] : rtranslations[lastAngle]) {
            double newX = x * cos(2 * pi / 5) - y * sin(2 * pi / 5);
            double newY = x * sin(2 * pi / 5) + y * cos(2 * pi / 5);
            rtranslations[angle].push_back({newX, newY, (72 + a) % 360});
        }
    }

    map<pair<ll, ll>, pair<double, double>> roundedToActual;
    map<Pos, ll> outCounts;
    const int maxArcCount = 35;
    outCounts[{0, 0, 90}] = 1;
    for(int i = 0; i < maxArcCount; i++) {
        cout << i << endl;
        map<Pos, ll> newMap;
        for(auto &[c, cnt] : outCounts) {
            auto &[x, y, ang] = c;
            auto &[dx, dy] = roundedToActual[{x, y}];
            for(auto &[xt, yt, na] : translations[ang]) {
                ll intx = round((dx + xt) * 10000);
                ll inty = round((dy + yt) * 10000);
                // cout << "-p-p-p-p-" << endl;
                // cout << ang << endl;
                // cout << x << ' ' << intx << endl;
                // cout << y << ' ' << inty << endl;
                // cout << dx << ' ' << dy << ' ' << xt << ' ' << yt << endl;
                // cout << "-p-p-p-p-" << endl;
                if (!roundedToActual.count({intx, inty})) {
                    roundedToActual[{intx, inty}] = {dx + xt, dy + yt};
                }
                Pos newPos = {intx, inty, na};
                newMap[newPos] += cnt;
            }
        }
        swap(newMap, outCounts);
    }

    map<Pos, ll> inCounts;
    inCounts[{0, 0, 90}] = 1;
    for(int i = 0; i < maxArcCount; i++) {
        cout << i << endl;
        map<Pos, ll> newMap;
        for(auto &[c, cnt] : inCounts) {
            auto &[x, y, ang] = c;
            auto &[dx, dy] = roundedToActual[{x, y}];
            for(auto &[xt, yt, na] : rtranslations[ang]) {
                ll intx = round((dx + xt) * 10000);
                ll inty = round((dy + yt) * 10000);
                if (!roundedToActual.count({intx, inty})) {
                    roundedToActual[{intx, inty}] = {dx + xt, dy + yt};
                }
                Pos newPos = {intx, inty, na};
                newMap[newPos] += cnt;
            }
        }
        swap(newMap, inCounts);
    }
    // cout << "OUTCOUNTS" << endl;
    // for(auto e : outCounts) {
    //     auto &[x, y, a] = e.first;
    //     cout << x << ' ' << y << ' ' << a << ' ' << e.second << endl;
    // }
    // cout << "INCOUNTS" << endl;
    // for(auto e : inCounts) {
    //     auto &[x, y, a] = e.first;
    //     cout << x << ' ' << y << ' ' << a << ' ' << e.second << endl;
    // }
    ll tot = 0;
    for(auto &[k, v] : inCounts) {
        auto &[x, y, angle] = k;
        int targetAngle = angle;
        Pos target = {x, y, targetAngle};
        auto it = outCounts.find(target);
        if (it != outCounts.end()) {
            tot += v * it->second;
        }
    }
    cout << tot << endl;
    return 0;
}