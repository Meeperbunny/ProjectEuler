#include <iostream>
#include <vector>
using namespace std;

using ll = long long;
const ll MOD = 20092010;
const int N = 2000;

using Matrix = vector<vector<ll>>;

Matrix mult(const Matrix &A, const Matrix &B) {
    int n = A.size(), m = B[0].size(), p = B.size();
    Matrix res(n, vector<ll>(m, 0));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < p; ++j) {
            ll a_ij = A[i][j];
            for (int q = 0; q < m; ++q) {
                res[i][q] = (res[i][q] + a_ij * B[j][q] % MOD) % MOD;
            }
        }
    }
    return res;
}

Matrix gen_transition() {
    Matrix transition(N, vector<ll>(N, 0));
    for (int i = 0; i < N - 1; ++i) {
        transition[i + 1][i] = 1;
    }
    transition[0][N - 1] = 1;
    transition[1][N - 1] = 1;
    return transition;
}

ll solve(ll k) {
    Matrix base(1, vector<ll>(N, 1));
    Matrix M = gen_transition();
    Matrix C = gen_transition();
    --k;
    while (k) {
        cout << k << endl;
        if (k & 1) {
            M = mult(C, M);
            --k;
        } else {
            C = mult(C, C);
            k /= 2;
        }
    }
    Matrix R = mult(base, M);
    for(int i = 0; i < R.size(); i++) {
        for(int q = 0; q < R[i].size(); q++) {
            cout << R[i][q] << ' ';
        } cout << endl;
    }
    return R[0][0];
}

int main() {
    cout << solve(1000000000000000000ll) << endl;
    return 0;
}
