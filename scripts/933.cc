#include <iostream>
#include <map>
#include <unordered_set>
#include <vector>
using namespace std;

using ll = unsigned long long;

const int N = 123;
const ll M = 1234567;

// map<pair<int, int>, int> grundy;
// map<pair<int, int>, ll> winning_moves;
//594164353164952
int grundy[124][10'001];
ll winning_moves[124][10'001];

#include <array>
#include <assert.h>
int mex(const array<int, 300> &a) {
    for(int i = 0; i < 300; ++i) {
        if (a[i] == 0) return i;
    }
    assert(false);
}

ll ways(int W, int H) {
    if (winning_moves[W][H] != -1)
    return winning_moves[W][H];

    for (int i = 1; i <= W; ++i) {
        for (int q = 1; q <= H; ++q) {
            if (winning_moves[i][q] != -1) continue;

            ll C = 0;
            if (i == 1 || q == 1) {
                grundy[i][q] = 0;
                winning_moves[i][q] = 0;
                continue;
            }

            array<int, 300> t;
            t.fill(0);
            for (int a = 1; a <= i / 2; ++a) {
                for (int b = 1; b <= q / 2; ++b) {
                    int nimber = grundy[a][b] ^ 
                                 grundy[i - a][b] ^ 
                                 grundy[a][q - b] ^ 
                                 grundy[i - a][q - b];
                    if (nimber == 0) {
                        int TA = 4;
                        if (a * 2 == i) TA /= 2;
                        if (b * 2 == q) TA /= 2;
                        C += TA;
                    }
                    t[nimber] = 1;
                }
            }
            int g = mex(t);
            grundy[i][q] = g;
            winning_moves[i][q] = C;
            if (q <= 123) {
                grundy[q][i] = g;
                winning_moves[q][i] = C;
            }
        }
    }
    return winning_moves[W][H];
}

ll tri(ll n) {
    return n * (n + 1) / 2;
}

int main() {
    for(int i = 0; i <= 123; i++) {
        for(int q = 0; q < 10'000; q++) {
            grundy[i][q] = -1;
            winning_moves[i][q] = -1;
        }
    }
    ll T = 0;
    for (int q = 1; q <= N; ++q) {
        vector<ll> z;
        int i = 0;
        int k = 100;
        int R = -1;
        while (true) {
            ++i;
            z.push_back(ways(q, i));
            if (i > k) {
                bool isg = true;
                for (int j = i - k; j < i - 1; ++j) {
                    if (z[j + 1] != q - 1 + z[j]) {
                        isg = false;
                        break;
                    }
                }
                if (isg) {
                    R = i - k + 1;
                    break;
                }
            }
        }

        ll CR = 0;
        for (int i = 1; i < R; ++i) {
            CR += ways(q, i);
        }

        ll L = M - R + 1;
        cout << "R " << q << " " << R << " " << CR << endl;
        CR += ways(q, R) * L + tri(L - 1) * (q - 1);
        cout << q << " " << CR << endl;
        T += CR;
    }
    cout << T << endl;
    return 0;
}

// 5707485980736903