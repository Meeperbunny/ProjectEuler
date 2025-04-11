#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

const int T = 100;
const int PC = 25;
const int INP = 3;
const int STATE_SIZE = 1 << PC;

int main() {
    using Float = long double;

    std::vector<std::vector<Float>> dp[2];
    dp[0].resize(STATE_SIZE, std::vector<Float>(INP + 2, 0));
    dp[1].resize(STATE_SIZE, std::vector<Float>(INP + 2, 0));

    dp[0][0][0] = 1;

    for (int p = 0; p < PC; ++p) {
        cout << p << endl;
        int total_spots = T - p;
        int cur = p % 2;
        int nxt = 1 - cur;

        // Clear next layer
        for (int s = 0; s < STATE_SIZE; ++s)
            for (int k = 0; k < INP + 1; ++k)
                dp[nxt][s][k] = 0;

        for (int s = 0; s < STATE_SIZE; ++s) {
            for (int k = 0; k <= INP; ++k) {
                if (dp[cur][s][k] == 0)
                    continue;

                int can_myself = 0, pc = 0;
                for (int i = 0; i < PC; ++i) {
                    if ((s >> i) & 1)
                        pc++;
                    else if (i == p)
                        can_myself = 1;
                }

                int primes_left = PC - pc;
                Float chance_prime = Float(primes_left - can_myself) / total_spots;
                Float chance_myself = Float(can_myself) / total_spots;
                Float chance_normal = 1 - (chance_prime + chance_myself);

                for (int i = 0; i < PC; ++i) {
                    if (!((s >> i) & 1)) {
                        int new_s = s | (1 << i);
                        if (i == p)
                            dp[nxt][new_s][k + 1] += dp[cur][s][k] / total_spots;
                        else
                            dp[nxt][new_s][k] += dp[cur][s][k] / total_spots;
                    }
                }

                dp[nxt][s][k] += dp[cur][s][k] * chance_normal;
            }
        }
    }

    Float result = 0;
    int final = PC % 2;
    for (int s = 0; s < STATE_SIZE; ++s)
        result += dp[final][s][INP];

    std::cout << 'a' << std::setprecision(40) << result << std::endl;
    return 0;
}
