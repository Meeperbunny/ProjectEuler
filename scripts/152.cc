#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <cmath>
#include <algorithm>
#include <climits>
#include <sstream>
#include <iomanip>
using namespace std;

// Use __int128 for 128-bit arithmetic.
typedef __int128 int128;

// Helper: Convert int128 to string for printing.
string toString(int128 x) {
    if(x == 0) return "0";
    bool neg = false;
    if(x < 0) { neg = true; x = -x; }
    string s;
    while(x > 0) {
        int digit = (int)(x % 10);
        s.push_back('0' + digit);
        x /= 10;
    }
    if(neg)
        s.push_back('-');
    reverse(s.begin(), s.end());
    return s;
}

// Compute gcd for int128.
int128 gcd(int128 a, int128 b) {
    while(b != 0) {
        int128 temp = a % b;
        a = b;
        b = temp;
    }
    return a;
}

// Compute lcm for int128.
int128 lcm_int128(int128 a, int128 b) {
    return a / gcd(a, b) * b;
}

// Prime factorization, similar to the Python pfs(n) routine.
vector<long long> pfs(long long n) {
    vector<long long> factors;
    for (long long i = 2; i * i <= n; i++) {
        while(n % i == 0) {
            factors.push_back(i);
            n /= i;
        }
    }
    if(n > 1)
        factors.push_back(n);
    return factors;
}

// Get largest prime factor.
long long get_lpf(long long n) {
    vector<long long> fac = pfs(n);
    if(fac.empty()) return n; // if n == 1
    long long maxp = 0;
    for (long long f : fac)
        maxp = max(maxp, f);
    return maxp;
}

// Get smallest prime factor.
long long get_spf(long long n) {
    vector<long long> fac = pfs(n);
    if(fac.empty()) return n;
    long long minp = LLONG_MAX;
    for (long long f : fac)
        minp = min(minp, f);
    return minp;
}

// Compute integer square root of int128 using binary search.
int128 isqrt(int128 x) {
    if(x < 0)
        return -1; // error for negative numbers
    int128 left = 0, right = 1;
    while(right * right <= x)
        right *= 2;
    while(left < right) {
        int128 mid = (left + right) / 2;
        if(mid * mid <= x)
            left = mid + 1;
        else
            right = mid;
    }
    return left - 1;
}

// Custom hash for int128 to use in unordered_map.
struct Int128Hash {
    std::size_t operator()(const int128 &x) const {
        unsigned long long low = (unsigned long long)x;
        unsigned long long high = (unsigned long long)(x >> 64);
        return std::hash<unsigned long long>()(low) ^ (std::hash<unsigned long long>()(high) << 1);
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // --- Parameters ---
    int N = 80;
    int t = 27;

    // --- Build s: integers from 3 to N ---
    vector<int> s;
    vector<int> badprimes = {19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79};
    for (int i = 3; i <= N; i++) {
        bool shouldAdd = true;
        for(auto p : badprimes) {
            if (i % p == 0) {
                shouldAdd = false;
            }
        }
        if (shouldAdd)
            s.push_back(i);
    }

    // --- Build counter "cc": for each e in s, count unique primes from pfs(e*e) ---
    map<long long, int> cc;
    for (int e : s) {
        long long num = (long long)e * e;
        vector<long long> fac = pfs(num);
        set<long long> unique_fac(fac.begin(), fac.end());
        for (long long p : unique_fac) {
            cc[p]++;
        }
    }

    // --- Build "validKs": for each k in s, if any prime factor in pfs(k*k)
    // appears in at least 2 numbers, then k is valid.
    vector<int> validKs;
    for (int k : s) {
        long long num = (long long)k * k;
        vector<long long> fac = pfs(num);
        set<long long> unique_fac(fac.begin(), fac.end());
        bool has = false;
        for (long long p : unique_fac) {
            if (cc[p] >= 2) {
                has = true;
                break;
            }
        }
        if(has) {
            validKs.push_back(k);
        }
    }

    // --- Compute least common multiple (lc) of denominators k*k for each valid k ---
    int128 lc = 1;
    for (int k : validKs) {
        int128 denom = (int128)k * k;
        lc = lcm_int128(lc, denom);
    }

    // --- Convert each fraction 1/(k*k) to integer value: lc / (k*k) ---
    vector<int128> nums;
    for (int k : validKs) {
        int128 denom = (int128)k * k;
        nums.push_back(lc / denom);
    }

    // --- Partition nums into two parts: l1 (first t elements) and l2 (remaining) ---
    vector<int128> l1, l2;
    for (size_t i = 0; i < nums.size(); i++) {
        if (i < (size_t)t)
            l1.push_back(nums[i]);
        else
            l2.push_back(nums[i]);
    }

    // --- Generate subset sums from l1 (only sums <= lc/2) with progress indicator ---
    unsigned long long totalL1 = (1ULL << l1.size()) - 1;
    unsigned long long countL1 = 0;
    unsigned long long lastProgressL1 = 0;
    vector<int128> subsetSums;
    subsetSums.push_back(0);

    for (int128 n : l1) {
        size_t ssz = subsetSums.size();
        for (size_t i = 0; i < ssz; i++) {
            int128 newSum = subsetSums[i] + n;
            if (newSum <= lc / 2)
                subsetSums.push_back(newSum);
            countL1++;
            unsigned long long currentProgress = (countL1 * 100) / totalL1;
            if (currentProgress > lastProgressL1) {
                lastProgressL1 = currentProgress;
                cout << "\rGenerating subset sums from l1: " 
                     << currentProgress << "% completed." << flush;
            }
        }
    }
    cout << "\rGenerating subset sums from l1: 100% completed." << "\n";

    // --- Map subset sums into frequency map with progress indicator ---
    unordered_map<int128, int, Int128Hash> ss;
    unsigned long long totalSubsetSums = subsetSums.size();
    unsigned long long lastProgressMap = 0;
    for (size_t i = 0; i < subsetSums.size(); i++) {
        ss[subsetSums[i]]++;
        unsigned long long currentProgress = (i * 100) / totalSubsetSums;
        if (currentProgress > lastProgressMap) {
            lastProgressMap = currentProgress;
            cout << "\rMapping subset sums: " 
                 << currentProgress << "% completed." << flush;
        }
    }
    cout << "\rMapping subset sums: 100% completed." << "\n";

    // --- Compute target tar = lc/2 - lc/4 ---
    int128 tar = lc / 2 - lc / 4;

    // --- Iterate over nonempty subsets of l2 with a finer-grained progress indicator ---
    int m = l2.size();
    int128 c_val = 0; // counter for the final result

    // Total combinations: 2^(m)
    unsigned long long totalL2 = (m > 0) ? (1ULL << m) : 0;
    unsigned long long lastProgressL2 = 0;
    if (totalL2 == 0) totalL2 = 1;  // Avoid division by zero

    // Here, we update progress every 0.01% (i.e. using hundredths of a percent)
    long long cnt = 0;
    long long ma = (1ULL << m);
    for (unsigned long long mask = 1; mask < ma; mask++) {
        cnt += 1;
        if ((cnt & 0b11111111111111111111) == 0) {
            cout << setprecision(10) << fixed << "Progress: " << double(cnt) / double(ma) << endl;
        }
        int128 sumSubset = 0;
        vector<int128> subsetElements;
        for (int j = 0; j < m; j++) {
            if (mask & (1ULL << j)) {
                sumSubset += l2[j];
                subsetElements.push_back(l2[j]);
            }
        }
        int128 comp = tar - sumSubset;
        if (ss.find(comp) != ss.end()) {
            // Build a temporary frequency map tt.
            map<long long, int> tt;
            // Print q values for each element in this combination.
            for (size_t i = 0; i < subsetElements.size(); i++) {
                int128 divisor = subsetElements[i];
                int128 quotient = lc / divisor;
                int128 sq = isqrt(quotient);
                long long q = (long long)sq; // assuming q fits in long long
                long long lp = get_lpf(q);
                tt[lp]++;
                // cout << q;
                // if (i < subsetElements.size() - 1)
                //     cout << ", ";
            }
            // cout << "\n";
            // // Print the tt map.
            // for (auto &p : tt) {
            //     cout << p.first << ": " << p.second << " ";
            // }
            // cout << "\n\n";
            c_val += ss[comp];
            // cout << "New count: " << toString(c_val) << endl;
        }
    }
    cout << "\rProcessing l2 subsets: 100% completed." << "\n";

    cout << "Final c: " << toString(c_val) << "\n";
    return 0;
}
