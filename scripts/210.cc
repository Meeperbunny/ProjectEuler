#include <iostream>
#include <cmath>
#include <cstdint>

using namespace std;

int64_t solve(int64_t n) {
    double sqrt2 = sqrt(2.0);
    int64_t B = 1 + 2 * n * (n + 1) - 2 * n - 1 - n * n / 2;
    double epsilon = 1e-8;
    double R = sqrt2 * (n / 4.0) / 2.0;

    for (int64_t c = 1; c < n / 2; ++c) {
        double y = sqrt(R * R - pow(R - c / sqrt2, 2));
        if (c & 1) {
            y += 1.0 / sqrt2;
        }
        B += static_cast<int64_t>(2 * floor((y - epsilon) / sqrt2));
    }

    return B;
}

int main() {
    cout << solve(1000000000) << endl;
    return 0;
}
