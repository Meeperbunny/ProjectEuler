#include <iostream>
#include <cmath>

using ld = long double;
ld pi = 3.14159265358979323846;

ld Approx[10000000];
ld approx(int i) {
    return Approx[i - 127000000];
}
ld aa(int n) {
    return 1.0 / std::sqrt(pi * n);
}

ld shift(ld last, int n, int i) {
    return last * 2.0 * (n - i) / (2.0 * n - i);
}

ld A(int n) {
    ld T = shift(approx(n) / 2.0, n, 0);
    ld B = approx(n - 1) / 2.0;
    for (int i = 0; i < n; i++) {
        T += B;
        B = shift(B, n - 1, i);
    }
    return T;
}


int main() {
    int k = 127000000;
    int j = 1 << 20; // 2^30
    ld v = 1.9999;

    std::cout << "Building" << std::endl;
    long double tmp = 0.5;
    Approx[1] = 0.5;
    for(int i = 2; i < 137000000; i++) {
        tmp = tmp * (2 * ld(i)) * (2 * ld(i) - 1) / ld(i) / ld(i) / 4.0;
        if (i >= 127000000)
            Approx[i - 127000000] = tmp;
        // std::cout << i << ' ' << Approx[i] << std::endl;
    }
    
    while (j >= 1) {
        int nk = k + j;
        std::cout << j << ' ' << nk << std::endl;
        if (A(nk) * v > 1.0) {
            k = nk;
        }
        j >>= 1;
    }
    k += 1;
    std::cout << A(7777) << std::endl;
    std::cout << k << " " << A(k) * v << std::endl;
    return 0;
}
