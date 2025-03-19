#include <bits/stdc++.h>

using ll = long long;
using namespace std;

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

vector<ll> ulam(ll a, ll b, ll n) {
    std::vector<ll> ulams{a, b};
    std::vector<ll> sieve(b);
    sieve[a - 1] = 1;
    sieve[b - 1] = 1;
    for (ll u = 2; ulams.size() < n; ) {
        sieve.resize(u + ulams[ulams.size() - 2], 0);
        for (ll i = 0; i < ulams.size() - 1; ++i)
            ++sieve[u + ulams[i] - 1];
        auto it = std::find(sieve.begin() + u, sieve.end(), 1);
        if (it == sieve.end())
            return {};
        u = (it - sieve.begin()) + 1;
        ulams.push_back(u);
    }
    return ulams;
}

vector<ll> OUlam(ll a, ll b, ll n) {
    vector<ll> seq;
    seq.push_back(a);
    seq.push_back(b);
    
    // Use an unordered_map to count representations.
    unordered_map<ll, int> cnt;
    cnt[a + b] = 1;
    
    ll to_check = max(a, b) + 1;
    // Continue until we have exactly n numbers.
    while (seq.size() < (size_t)n) {
        while (true) {
            // If candidate appears exactly once as a sum of two earlier (or same newly added) terms...
            if (cnt[to_check] == 1) {
                seq.push_back(to_check);
                // Update counts: add the new sums with every element already in the sequence.
                for (ll x : seq) {
                    cnt[to_check + x]++;
                }
                to_check++;
                break;
            } else {
                to_check++;
            }
        }
    }
    return seq;
}

// Generate the first n Ulam numbers for given starting values a and b.
vector<ll> Ulam(ll a, ll b, ll n) {
    vector<ll> seq;
    seq.push_back(a);
    seq.push_back(b);
    
    // Use an unordered_map to count representations.
    unordered_map<ll, int> cnt;
    vector<ll> oneCounts;
    cnt[a + b] = 1;
    oneCounts.push_back(a + b);
    
    // Continue until we have exactly n numbers.
    while (seq.size() < (size_t)n) {
        while(oneCounts.back() < seq.back()) {
            oneCounts.pop_back();
        }
        ll nxt = oneCounts.back();
        oneCounts.pop_back();
        
        // Update counts: add the new sums with every element already in the sequence.
        for (ll x : seq) {
            ll added = nxt + x;            
            ll c = cnt[added];
            if (c == 0) {
                auto it = std::lower_bound(oneCounts.begin(), oneCounts.end(), added, std::greater<int>());
                oneCounts.insert(it, added);
                cnt[added]++;
            }
            else if (c == 1) {
                oneCounts.erase(std::remove(oneCounts.begin(), oneCounts.end(), added), oneCounts.end());
                cnt[added]++;
            }
        }
        seq.push_back(nxt);
    }
    return seq;
}

std::vector<ll> ULAM(ll a, ll b, ll n) {
    ll upper = n * 2;
    std::vector<ll> V(upper, 0);
    std::vector<ll> W(upper, 1);

    // Set the initial conditions.
    V[a - 1] = 1;
    V[b - 1] = 1;
    W[a - 1] = 0;
    W[b - 1] = 0;
    
    ll k = 2;
    
    // Loop until no new element is found or k exceeds half of upper.
    while (k < upper / 2) {
        // Update V[k:2*k-1] (Python slice: indices k to 2*k-2) using the given boolean expression.
        // There are exactly k-1 elements in the slice.
        for (ll i = 0; i < k - 1; i++) {
            // Here, for each i, the corresponding elements are:
            //   - V[k + i] from V[k:2*k-1]
            //   - V[i] from V[0:k-1]
            //   - W[k + i] from W[k:2*k-1]
            ll a_val = V[k + i];
            ll b_val = V[i];
            ll c_val = W[k + i];
            
            // The Python expression:
            // ((not a) and b and c) or (a and (not b) and (not c)) or (a and (not b) and c)
            // Simplifies to:
            // if (!a_val) then (b_val && c_val)
            // else (if a_val then (!b_val) )
            ll newV = 0;
            if (!a_val) {
                newV = (b_val && c_val) ? 1 : 0;
            } else {
                newV = (!b_val) ? 1 : 0;
            }
            V[k + i] = newV;
        }
        
        // Update W[k:2*k-1] (same indices) using the expression: (not a) and b,
        // where a comes from V[0:k-1] and b comes from W[k:2*k-1].
        for (ll i = 0; i < k - 1; i++) {
            ll a_val = V[i];
            ll b_val = W[k + i];
            ll newW = (!a_val && b_val) ? 1 : 0;
            W[k + i] = newW;
        }
        
        // Build a list L of j values (Python: j for j in range(k+1, upper) if V[j-1] == 1)
        std::vector<ll> L;
        for (ll j = k + 1; j < upper; j++) {
            if (V[j - 1] == 1) {
                L.push_back(j);
            }
        }
        
        // If no new indices were found, break the loop.
        if (L.empty()) {
            break;
        } else {
            // Set k to the minimum element in L.
            k = *std::min_element(L.begin(), L.end());
        }
    }
    
    // Build the result list ls: all indices i+1 where V[i]==1.
    std::vector<ll> ls;
    for (size_t i = 0; i < V.size(); i++) {
        if (V[i] == 1) {
            ls.push_back(i + 1);
        }
    }
    // Return only the first half of ls (like Python slicing ls[0:len(ls)//2])
    ls.resize(ls.size() / 2);
    return ls;
}

std::vector<ll> ulam_bit(ll a, ll b, ll n) {
    // Create a vector of size n, all initialized to 0.
    std::vector<ll> v(n, 0);
    
    // Mark the arbitrary starting numbers (1-indexed).
    v[a - 1] = 1;
    v[b - 1] = 1;
    
    // Start candidate poller at b.
    ll k = b;
    
    while (k < n) {
        // Determine the number of iterations:
        // Python does: for i in range(min(k - 1, n - k))
        ll limit = std::min(k - 1, n - k);
        for (ll i = 0; i < limit; i++) {
            // If v[i] is 1 (i.e. (v[i] == 1) is true),
            // then add 1 to v[i+k].
            if (v[i] == 1) {
                v[i + k] += 1;
            }
        }
        // Move to the next candidate.
        k++;
        // Skip numbers that do not have a unique representation (v[...] != 1).
        while ((k - 1) < n && v[k - 1] != 1) {
            k++;
        }
    }
    
    // Build the list of Ulam numbers: indices where v[i] is 1.
    std::vector<ll> result;
    for (ll i = 0; i < n; i++) {
        if (v[i] == 1) {
            result.push_back(i + 1);  // Convert from 0-indexed to 1-indexed.
        }
    }
    
    return result;
}

// Compute the successive differences of a sequence.
vector<ll> diff(const vector<ll>& s) {
    vector<ll> d;
    for (size_t i = 0; i + 1 < s.size(); i++) {
        d.push_back(s[i + 1] - s[i]);
    }
    return d;
}

// Given a starting Ulam sequence U(2, b) with b odd and >= 5, find the kth Ulam number using periodicity.
ll solve(ll a, ll b, ll k) {
    // Check preconditions (for U(2, 2k+1) with k>=2).
    assert(a == 2 && (b % 2 == 1) && b >= 5);

    ll to_try = 2'000;      // initial number of Ulam numbers to generate
    ll times_to_check = 3; // number of periods we want to see repeating
    ll max_p_len = (to_try * 0.95) / times_to_check;   // maximum period length to try
    
    vector<ll> seq;

    seq.push_back(a);
    seq.push_back(b);
    
    // Use an unordered_map to count representations.
    unordered_map<ll, int> cnt;
    vector<ll> oneCounts;
    cnt[a + b] = 1;
    oneCounts.push_back(a + b);
    
    int p_len = -1;
    ll inc = -1;
    
    vector<ll> d, rdiff;
    while (true) {
        seq = ulam_bit(a, b, to_try);
        
        d = diff(seq);
        rdiff = d;
        reverse(rdiff.begin(), rdiff.end());
        StringHash sh(rdiff);

        bool found = false;
        // Try candidate period lengths from 1 to max_p_len.
        for (int L = 16; L <= max_p_len; L++) {
            bool w = true;
            // We need at least (times_to_check+1) blocks of length L in rdiff.
            if ((times_to_check + 1) * L > (int)rdiff.size()) {
                w = false;
                break;
            } else {
                // Compare successive blocks of length L.
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
    ll tot = 0;
    // For n from 2 to 10, we solve for U(2, 2*n+1) and add the kth (10^11-th) Ulam number.
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

/*
 g++ scripts/167.cc -o 167 && ./167.exe
1 2 3 4 7 9 12 15 17 20 23 25 28 31 33 36 39 41 44 47 49 52 55 57 60 63 65 68 71 73 76 79 81 84 87 89 92 95 97 100 103 105 108 111 113 116 119 121 124 127 129 132 135 137 140 143 145 148 151 153 156 159 161 164 167 169 172 175 177 180 183 185 188 191 193 196 199 201 204 207 209 212 215 217 220 223 225 228 231 233 236 239 241 244 247 249 252 255 257 260
Solving U(2, 5)
Found p_len: 32 and inc: 126
Got: 393749999981
Solving U(2, 7)
Found p_len: 26 and inc: 126
Got: 484615384605
Solving U(2, 9)
Period not found under to_try: 500 and max_p_len: 80
Period not found under to_try: 1000 and max_p_len: 160
Period not found under to_try: 2000 and max_p_len: 320
Found p_len: 444 and inc: 1778
Got: 400450450395
Solving U(2, 11)
Period not found under to_try: 500 and max_p_len: 80
Period not found under to_try: 1000 and max_p_len: 160
Period not found under to_try: 2000 and max_p_len: 320
Period not found under to_try: 4000 and max_p_len: 640
Period not found under to_try: 8000 and max_p_len: 1280
Found p_len: 1628 and inc: 6510
Got: 399877149781
Solving U(2, 13)
Period not found under to_try: 500 and max_p_len: 80
Period not found under to_try: 1000 and max_p_len: 160
Period not found under to_try: 2000 and max_p_len: 320
Period not found under to_try: 4000 and max_p_len: 640
Period not found under to_try: 8000 and max_p_len: 1280
Period not found under to_try: 16000 and max_p_len: 2560
Period not found under to_try: 32000 and max_p_len: 5120
Found p_len: 5906 and inc: 23622
Got: 399966136001
Solving U(2, 15)
Found p_len: 80 and inc: 510
Got: 637499999951
Solving U(2, 17)
Period not found under to_try: 500 and max_p_len: 80
Period not found under to_try: 1000 and max_p_len: 160
Period not found under to_try: 2000 and max_p_len: 320
Period not found under to_try: 4000 and max_p_len: 640
Period not found under to_try: 8000 and max_p_len: 1280
Period not found under to_try: 16000 and max_p_len: 2560
Period not found under to_try: 32000 and max_p_len: 5120
Period not found under to_try: 64000 and max_p_len: 10240
Period not found under to_try: 128000 and max_p_len: 20480
*/

/*
$ g++ scripts/167.cc -o 167 && ./167.exe
1 2 3 4 6 8 11 13 16 18 26 28 36 38 47 48 53 57 62 69 72 77 82 87 97 99 102 106 114 126 131 138 145 148 155 175 177 180 182 2 309 316 319 324 339 341 356 358 363 370 382 390 400 402 409 412 414 429 431 434 441 451 456 483 485 497 502 522 524 544 54
690
Solving U(2, 5)
Found p_len: 32 and inc: 126
Got: 393749999981
Solving U(2, 7)
Found p_len: 26 and inc: 126
Got: 484615384605
Solving U(2, 9)
Found p_len: 444 and inc: 1778
Got: 400450450395
Solving U(2, 11)
Period not found under to_try: 2000 and max_p_len: 633
Period not found under to_try: 4000 and max_p_len: 1266
Found p_len: 1628 and inc: 6510
Got: 399877149781
Solving U(2, 13)
Got: 399966136001
Solving U(2, 15)
Found p_len: 80 and inc: 510
Got: 637499999951
Solving U(2, 17)
Period not found under to_try: 128000 and max_p_len: 40512
Period not found under to_try: 256000 and max_p_len: 81024
Found p_len: 126960 and inc: 507842
Got: 400001574629
Solving U(2, 19)
Period not found under to_try: 2000 and max_p_len: 633
Period not found under to_try: 4000 and max_p_len: 1266
Period not found under to_try: 8000 and max_p_len: 2532
Period not found under to_try: 16000 and max_p_len: 5064
Period not found under to_try: 32000 and max_p_len: 10128
Period not found under to_try: 64000 and max_p_len: 20256
Period not found under to_try: 128000 and max_p_len: 40512
Period not found under to_try: 256000 and max_p_len: 81024
Period not found under to_try: 512000 and max_p_len: 162048
*/