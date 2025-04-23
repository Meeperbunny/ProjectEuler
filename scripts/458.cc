#include <iostream>
#include <vector>
#include <array>
#include <unordered_map>
#include <unordered_set>
using ll = long long;

ll factorial(int n) {
    ll f = 1;
    for(int i = 1; i <= n; ++i) f *= i;
    return f;
}

ll string_to_num(const std::array<int,7>& s) {
    std::unordered_map<int,int> seen;
    ll h = 0, cc = 1;
    for(int c : s) {
        int id;
        auto it = seen.find(c);
        if(it == seen.end()) {
            id = seen.size();
            seen.emplace(c, id);
        } else {
            id = it->second;
        }
        h = h * cc + id;
        cc++;
    }
    return h;
}

std::vector<std::vector<ll>> mult(
    const std::vector<std::vector<ll>>& A,
    const std::vector<std::vector<ll>>& B,
    ll mod
) {
    int m = A.size(), n = B.size(), p = B[0].size();
    std::vector<std::vector<ll>> res(m, std::vector<ll>(p));
    for(int i = 0; i < m; ++i)
        for(int j = 0; j < n; ++j)
            for(int q = 0; q < p; ++q) {
                res[i][q] += A[i][j] * B[j][q];
                if(mod) res[i][q] %= mod;
            }
    return res;
}

std::vector<std::vector<ll>> matpow(
    std::vector<std::vector<ll>> m,
    ll k,
    ll mod
) {
    std::vector<std::vector<ll>> b = m;
    k -= 1;
    while(k) {
        std::cout << k << std::endl;
        if(k & 1) {
            m = mult(b, m, mod);
            k--;
        } else {
            b = mult(b, b, mod);
            k >>= 1;
        }
    }
    return m;
}

int main() {
    int n = 7;
    ll fac = factorial(n);

    std::vector<std::vector<ll>> base(1, std::vector<ll>(fac));
    std::vector<std::vector<ll>> transition(fac, std::vector<ll>(fac));
    std::unordered_set<ll> seen_codes;
    std::array<int,7> st;

    ll state_count = 1;
    for(int i = 0; i < n; ++i) state_count *= 7;

    for(ll i = 0; i < state_count; ++i) {
        ll tmp = i;
        for(int q = 0; q < n; ++q) {
            st[q] = tmp % 7;
            tmp /= 7;
        }

        ll code = string_to_num(st);
        if(code != fac - 1) base[0][code]++;
        if(seen_codes.count(code)) continue;
        seen_codes.insert(code);

        if(code != fac - 1) {
            for(int new_end = 0; new_end < 7; ++new_end) {
                std::array<int,7> n_st;
                for(int q = 0; q < n - 1; ++q) n_st[q] = st[q + 1];
                n_st[n - 1] = new_end;
                ll new_code = string_to_num(n_st);
                if(new_code != fac - 1)
                    transition[code][new_code]++;
            }
        }
    }

    ll sum_base = 0;
    for(ll i = 0; i < fac - 1; ++i) sum_base += base[0][i];
    std::cout << sum_base << '\n';

    ll mod = 1000000000;
    ll N = 1000000000000LL;
    auto Mpow = matpow(transition, N - n, mod);
    auto res = mult(base, Mpow, mod);

    ll sum_res = 0;
    for(ll i = 0; i < fac - 1; ++i) sum_res += res[0][i];
    std::cout << sum_res << '\n';

    return 0;
}
