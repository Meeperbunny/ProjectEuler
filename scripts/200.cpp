#include <bits/stdc++.h>
using namespace std;
#define HEADER ios::sync_with_stdio(0);cin.tie(0);if (fopen("file.in", "r")) {freopen("file.in", "r+", stdin);};
#define all(v) v.begin(), v.end()
using ll = unsigned long long;
void dbg_out() { cerr << endl; }
template<typename Head, typename... Tail> void dbg_out(Head H, Tail... T) { cerr << ' ' << H; dbg_out(T...); }

#ifdef IAN_DEBUG
#define dbg(...) cerr << '[' << __FILE__ << ':' << __LINE__ << "] (" << #__VA_ARGS__ << "):", dbg_out(__VA_ARGS__)
#else
#define dbg(...)
#endif

#define MAXPRIME 100000000
bool sieve[MAXPRIME + 1];

// Function to perform modular exponentiation: (base^exp) % mod
long long modular_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    base = base % mod;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        exp = exp >> 1; // exp = exp / 2
        base = (base * base) % mod;
    }
    return result;
}

// Miller-Rabin primality test
bool miller_rabin(long long n, int k = 8) {
    if (n <= 1) {
        return false;
    }
    if (n == 2 || n == 3) {
        return true;
    }
    
    long long d = n - 1;
    int s = 0;
    
    // Find d such that n-1 = d * 2^s
    while (d % 2 == 0) {
        d /= 2;
        s++;
    }
    
    // Witness loop
    for (int i = 0; i < k; i++) {
        long long a = 2 + rand() % (n - 3); // Random number in [2, n-2]
        long long x = modular_pow(a, d, n);
        if (x == 1 || x == n - 1) {
            continue;
        }
        
        bool composite = true;
        for (int r = 0; r < s - 1; r++) {
            x = modular_pow(x, 2, n);
            if (x == n - 1) {
                composite = false;
                break;
            }
        }
        
        if (composite) {
            return false;
        }
    }
    
    return true;
}

bool isprime(ll n) {
    if (n <= 1) return false;
    for(ll i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

void TC() {
    vector<ll> primes;
    memset(sieve, 0, sizeof(sieve));
    for(ll i = 2; i <= MAXPRIME; i++) {
        if (!sieve[i]) {
            primes.push_back(i);
            for(ll q = 2 * i; q <= MAXPRIME; q += i) {
                sieve[q] = 1;
            }
        }
    }
    set<pair<int, int>> s;
    using ps = pair<ll, pair<ll, ll>>;
    priority_queue<ps, vector<ps>, greater<ps>> Q;
    s.insert({0, 0});
    Q.push({32, {0, 0}});
    int target = 200;
    ll lastnum = -1;
    while(target) {
        ps c(Q.top());
        ll &num = c.first;
        ll &a = c.second.first, b = c.second.second;
        // dbg(a, b);
        Q.pop();
        // Push adjacent
        // Add one to a, add one to b
        if (!s.count({a + 1, b})) {
            Q.push({primes[a + 1] * primes[a + 1] * primes[b] * primes[b] * primes[b], {a + 1, b}});
            s.insert({a + 1, b});
        }
        if (!s.count({a, b + 1})) {
            Q.push({primes[a] * primes[a] * primes[b + 1] * primes[b + 1] * primes[b + 1], {a, b + 1}});
            s.insert({a, b + 1});
        }
        // Eval if f != s
        if (a != b) {
            // Check
            ll lower = 1;
            bool isg = false;
            while(num / lower > 199) {
                if (ll(num / lower) % 1000 == 200) {
                    isg = true;
                    break;
                }
                lower *= 10;
            }

            if (isg) {
                string str = to_string(num);
                // Change each digit
                isg = true;
                for(int i = 0; isg && i < str.size(); i++) {
                    char b = str[i];
                    for(int ch = '0'; isg && ch <= '9'; ch++) {
                        // if (ch == b) continue;;
                        str[i] = ch;
                        ll newnum = stoll(str);
                        // if (isprime(newnum) != miller_rabin(newnum)) {
                            
                        //     dbg(num, str, newnum, isprime(newnum), miller_rabin(newnum));
                        //     assert(false);
                        // }
                        if (isprime(newnum)) {
                            isg = false;
                        }
                    }
                    str[i] = b;
                }
                cout << str << ' ' << isg << endl;
                if (isg) {
                    target--;
                    lastnum = num;
                }
            }
        }
    }
    cout << lastnum << endl;
}

int main() {
    HEADER;
    int T = 1;
    // cin >> T;
    for (int t = 0; t < T; t++) {
        TC();
    }
    return 0;
}