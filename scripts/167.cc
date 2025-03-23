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

template<const int64_t &MOD>
struct _mint {
    int val;
 
    _mint(int64_t v = 0) {
        if (v < 0) v = v % MOD + MOD;
        if (v >= MOD) v %= MOD;
        val = int(v);
    }
 
    _mint(uint64_t v) {
        if (v >= MOD) v %= MOD;
        val = int(v);
    }
 
    _mint(int v) : _mint(int64_t(v)) {}
    _mint(unsigned v) : _mint(uint64_t(v)) {}
 
    explicit operator int() const { return val; }
    explicit operator unsigned() const { return val; }
    explicit operator int64_t() const { return val; }
    explicit operator uint64_t() const { return val; }
    explicit operator double() const { return val; }
    explicit operator long double() const { return val; }
 
    _mint& operator+=(const _mint &other) {
        val -= MOD - other.val;
        if (val < 0) val += MOD;
        return *this;
    }
 
    _mint& operator-=(const _mint &other) {
        val -= other.val;
        if (val < 0) val += MOD;
        return *this;
    }
 
    static unsigned fast_mod(uint64_t x, unsigned m = MOD) {
#if !defined(_WIN32) || defined(_WIN64)
        return unsigned(x % m);
#endif
        // Optimized mod for Codeforces 32-bit machines.
        // x must be less than 2^32 * m for this to work, so that x / m fits in an unsigned 32-bit int.
        unsigned x_high = unsigned(x >> 32), x_low = unsigned(x);
        unsigned quot, rem;
        asm("divl %4\n"
            : "=a" (quot), "=d" (rem)
            : "d" (x_high), "a" (x_low), "r" (m));
        return rem;
    }
 
    _mint& operator*=(const _mint &other) {
        val = fast_mod(uint64_t(val) * other.val);
        return *this;
    }
 
    _mint& operator/=(const _mint &other) {
        return *this *= other.inv();
    }
 
    friend _mint operator+(const _mint &a, const _mint &b) { return _mint(a) += b; }
    friend _mint operator-(const _mint &a, const _mint &b) { return _mint(a) -= b; }
    friend _mint operator*(const _mint &a, const _mint &b) { return _mint(a) *= b; }
    friend _mint operator/(const _mint &a, const _mint &b) { return _mint(a) /= b; }
 
    _mint& operator++() {
        val = val == MOD - 1 ? 0 : val + 1;
        return *this;
    }
 
    _mint& operator--() {
        val = val == 0 ? MOD - 1 : val - 1;
        return *this;
    }
 
    _mint operator++(int) { _mint before = *this; ++*this; return before; }
    _mint operator--(int) { _mint before = *this; --*this; return before; }
 
    _mint operator-() const {
        return val == 0 ? 0 : MOD - val;
    }
 
    friend bool operator==(const _mint &a, const _mint &b) { return a.val == b.val; }
    friend bool operator!=(const _mint &a, const _mint &b) { return a.val != b.val; }
    friend bool operator<(const _mint &a, const _mint &b) { return a.val < b.val; }
    friend bool operator>(const _mint &a, const _mint &b) { return a.val > b.val; }
    friend bool operator<=(const _mint &a, const _mint &b) { return a.val <= b.val; }
    friend bool operator>=(const _mint &a, const _mint &b) { return a.val >= b.val; }
 
    static const int64_t SAVE_INV = int(1e6) + 5;
    static _mint save_inv[SAVE_INV];
 
    static void prepare_inv() {
        // Ensures that MOD is prime, which is necessary for the inverse algorithm below.
        for (int64_t p = 2; p * p <= MOD; p += p % 2 + 1)
            assert(MOD % p != 0);
 
        save_inv[0] = 0;
        save_inv[1] = 1;
 
        for (int i = 2; i < SAVE_INV; i++)
            save_inv[i] = save_inv[MOD % i] * (MOD - MOD / i);
    }
 
    _mint inv() const {
        if (save_inv[1] == 0)
            prepare_inv();
 
        if (val < SAVE_INV)
            return save_inv[val];
 
        _mint product = 1;
        int v = val;
 
        do {
            product *= MOD - MOD / v;
            v = MOD % v;
        } while (v >= SAVE_INV);
 
        return product * save_inv[v];
    }
 
    _mint pow(int64_t p) const {
        if (p < 0)
            return inv().pow(-p);
 
        _mint a = *this, result = 1;
 
        while (p > 0) {
            if (p & 1)
                result *= a;
 
            p >>= 1;
 
            if (p > 0)
                a *= a;
        }
 
        return result;
    }
 
    friend ostream& operator<<(ostream &os, const _mint &m) {
        return os << m.val;
    }
};
 
template<const int64_t &MOD> _mint<MOD> _mint<MOD>::save_inv[_mint<MOD>::SAVE_INV];
 
// const int64_t MOD = 998244353;
const int64_t MOD = int64_t(1e9) + 7;
using mint = _mint<MOD>;
 
struct StringHash {
    vector<mint> prefixHash;
    vector<mint> memo;
    ll inc;
    StringHash(vector<ll> seq) {
        inc = *max_element(seq.begin(), seq.end()) + 1;
        prefixHash = vector<mint>(seq.size() + 1);
        memo = vector<mint>(seq.size() + 1, 0);
        prefixHash[0] = 0;
        for(int i = 1; i <= seq.size(); i++) {
            prefixHash[i] = prefixHash[i - 1] * mint(inc) + mint(seq[i - 1]);
        }
    }
    bool comp(int l1, int r1, int l2, int r2) {
        if (r1 - l1 != r2 - l2) return false;
        if (l1 > l2) {
            swap(l1, l2);
            swap(r1, r2);
        }
        if (memo[r1 - l1 + 1] == 0) memo[r1 - l1 + 1] = mint(inc).pow(r1 - l1 + 1);
        mint p = memo[r1 - l1 + 1];
        mint h1 = prefixHash[r1 + 1] - prefixHash[l1] * p;
        mint h2 = prefixHash[r2 + 1] - prefixHash[l2] * p;
 
        return h1 == h2;
    }
    mint hash(int l1, int r1) {
        if (memo[r1 - l1 + 1] == 0) memo[r1 - l1 + 1] = mint(inc).pow(r1 - l1 + 1);
        mint p = memo[r1 - l1 + 1];
        return prefixHash[r1 + 1] - prefixHash[l1] * mint(inc).pow(r1 - l1 + 1);
    }
};

// Wavelength for U(1, 2)
const double lambda = 2.44344296778474;

struct Ulam {
    ll a, b, ind, cand;
    vector<ll> smaller, seq;
    unordered_set<ll> nums;
    map<double, ll> residue;
    double l;
    Ulam(ll a, ll b, double l) : a(a), b(b), l(l) {
        this->insert(a);
        this->insert(b);
        cand = b + 1;
        ind = 0;
    }

    void next() {
        for (;;) {
            ll tcnts = 0;
            double rt = fmod(cand, l);
            // cout << setprecision(5) << fixed << "Cand " << cand << " searching " << std::format("[{}, {}] and [{}, {}]", 
            //         0, rt * 0.5, 0.5 * (rt + l), l) << endl;
            auto halfIt = residue.lower_bound(rt * 0.5);
            bool w = true;
            for(auto it = residue.begin(); w && it != halfIt; it++) {
                ll num = it->second; {
                    tcnts += nums.count(cand - num);
                    if (tcnts >= 2) {
                        w = false;
                        break;
                    }
                }
            }
            double rtl = 0.5 * (rt + l);
            auto upper = residue.upper_bound(l);
            for(auto it = residue.lower_bound(rtl); w && it != upper; it++) {
                ll num = it->second;
                if (cand - num != num) {
                    tcnts += nums.count(cand - num);
                    if (tcnts >= 2) {
                        w = false;
                        break;
                    }
                }
            }
            cand++;
            if (tcnts == 1) {
                insert(cand - 1);
                return;
            }
        }
    }

    void insert(ll a) {
        nums.insert(a);
        seq.push_back(a);
        residue.insert({fmod(a, l), a});
    }

    static vector<ll> Generate(ll n, ll a, ll b, double l) {
        auto U = Ulam(a, b, l);
        while(U.seq.size() < n) {
            U.next();
        }
        return U.seq;
    }
};

vector<ll> diff(const vector<ll>& v) {
    vector<ll> r(v.size() - 1);
    for(int i = 0; i < v.size() - 1; i++) {
        r[i] = v[i + 1] - v[i];
    }
    return r;
}

ll solve(ll a, ll b, ll k) {
    assert(a == 2 && (b % 2 == 1) && b >= 5);
    
    // Want an estimate on lambda. Will generate sequences and try to find one
    // double bestLambda = lambda;
    // ll bestTime = LLONG_MAX;
    // double increase = 0.001;
    // ll toGen = 2'000;
    // double la = 0.1;
    // for(double sl = increase; sl < 5.0; sl += increase) {
    //     if (sl > la) {
    //         cout << sl << endl;
    //         la *= 2;
    //     }
    //     auto st = chrono::high_resolution_clock::now();
    //     Ulam::Generate(toGen, a, b, sl);
    //     auto en = chrono::high_resolution_clock::now();
    //     ll time = chrono::duration_cast<chrono::nanoseconds>(en - st).count();
    //     // cout << sl << ' ' << time << endl;
    //     if (time < bestTime) {
    //         bestTime = time;
    //         bestLambda = sl;
    //     }
    // }
    // cout << format("Best lambda for U({}, {}) is {}", a, b, bestLambda) << endl;
    // return 0;

    ll to_try = 10'000;
    ll times_to_check = 3;
    ll max_p_len = (to_try * 0.95) / times_to_check;

    int p_len = -1;
    ll inc = -1;
    
    vector<ll> seq;
    vector<ll> d;
    while (true) {
        seq = Ulam::Generate(to_try, a, b, 0.016000000000000000);
        d = diff(seq);
        auto rdiff(d);
        reverse(rdiff.begin(), rdiff.end());
        StringHash sh(rdiff);

        bool found = false;
        for (int L = 16; L <= max_p_len; L++) {
            bool w = true;
            if ((times_to_check + 1) * L > (int)rdiff.size()) {
                w = false;
                break;
            } else {
                for (int q = 0; q < times_to_check; q++) {
                    ll lower = q * L;
                    ll upper = (q + 1) * L;
                    ll e = (q + 2) * L;
                    
                    w = sh.comp(lower, upper - 1, upper, e - 1);
                    if (!w) break;
                }
            }
            if (w) {
                p_len = L;
                inc = 0;
                // Compute the increment as the sum of one period block.
                for (int i = 0; i < L; i++) {
                    inc += rdiff[i];
                }
                found = true;
                break;
            }
        }
        if (!found) {
            cout << "Period not found under to_try: " << to_try 
                 << " and max_p_len: " << max_p_len << "\n";
            // Increase parameters and recompute the sequence.
            to_try *= 2;
            max_p_len *= 2;
        } else {
            cout << "Found p_len: " << p_len << " and inc: " << inc << "\n";
            break;
        }
    }
    
    // Now use the detected period to extrapolate to the kth element.
    ll final_el = seq.back();     // current last element in the computed sequence
    ll curr_pos = seq.size();       // number of Ulam numbers computed so far
    ll period = p_len;              // period length (in number of differences)
    
    // Jump forward as many whole periods as possible.
    ll times = (k - curr_pos) / period;
    final_el += inc * times;
    curr_pos += times * period;
    
    // Continue one difference at a time for the remainder.
    int i = d.size() - period; // start at the beginning of the period in d
    while (curr_pos < k) {
        final_el += d[i];
        curr_pos++;
        i++;
    }
    
    return final_el;
}

int main() {
    // // TODO: Solve it.
    // const int k = 100000;
    // cout << "Generating" << endl;
    // auto st = chrono::high_resolution_clock::now();
    // auto nums = Ulam::Generate(k, 2, 11, lambda);
    // auto en = chrono::high_resolution_clock::now();
    // cout << "Generating first k = " << k << " took " << chrono::duration_cast<chrono::milliseconds>(en - st) << "." << endl;
    // st = chrono::high_resolution_clock::now();
    // nums = Ulam::Generate(k, 2, 11, 0.016000000000000000);
    // en = chrono::high_resolution_clock::now();
    // cout << "Generating first k = " << k << " took " << chrono::duration_cast<chrono::milliseconds>(en - st) << "." << endl;

    ll tot = 0;
    // For n from 2 to 10, we solve for U(2, 2*n+1) and add the kth (10^11-th) Ulam number.
    // cout << solve(1, 2, 1000000) << endl;
    for (int n = 2; n <= 10; n++) {
        ll b = 2 * n + 1;
        cout << "Solving U(2, " << b << ")" << "\n";
        ll sol = solve(2, b, 100000000000LL);
        tot += sol;
        cout << "Got: " << sol << "\n";
    }
    cout << tot << "\n";
    return 0;
}