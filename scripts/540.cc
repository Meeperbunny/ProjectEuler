#include <iostream>

// Helper function to compute gcd of two numbers.
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    
    long long K = 314159265358;

    long long C = 0;
    for (long long n = 1; n * n < K; ++n) {
        if (n & 1LL) {  // n is odd
            for (long long q = 2; q < n; q += 2) {
                if (n * n + q * q > K)
                    break;
                if (gcd(q, n) == 1)
                    ++C;
            }
        } else {  // n is even
            for (long long q = 1; q < n; q += 2) {
                if (n * n + q * q > K)
                    break;
                if (gcd(q, n) == 1)
                    ++C;
            }
            // The original pseudocode has a commented line:
            // C += TOT[n];
            // Without more context for TOT, it is left as a comment.
        }
    }

    std::cout << C << "\n";
    return 0;
}
