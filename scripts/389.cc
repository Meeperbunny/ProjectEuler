#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <numeric>
#include <bits/stdc++.h>
using namespace std;

// Simulate a dice roll for a k‐sided die using the provided RNG.
int dice(int k, std::mt19937 &rng) {
    std::uniform_int_distribution<int> dist(1, k);
    return dist(rng);
}

// Perform one trial of the nested dice process.
int trial(std::mt19937 &rng) {
    int T = dice(4, rng);
    int C = 0;
    for (int i = 0; i < T; i++) {
        C += dice(6, rng);
    }
    int CC = 0;
    for (int i = 0; i < C; i++) {
        CC += dice(8, rng);
    }
    int NT = 0;
    for (int i = 0; i < CC; i++) {
        NT += dice(12, rng);
    }
    int EE = 0;
    for (int i = 0; i < NT; i++) {
        EE += dice(20, rng);
    }
    return EE;
}

int main() {
    // Set up random generator seeded with current time.
    std::mt19937 rng(static_cast<unsigned int>(std::chrono::steady_clock::now().time_since_epoch().count()));

    // The dice sides for each stage: 4-sided, 6-sided, 8-sided, 12-sided.
    std::vector<int> D = {4, 6, 8, 12, 20};

    // Compute MA = (product of D) + 1.
    int MA = 1;
    for (int e : D) {
        MA *= e;
    }
    MA += 1; // MA is used as the array size for probability distributions.

    // Create a 2D vector "probs" of size (number of stages) x MA, initialized to 0.
    int stages = D.size();
    std::vector<std::vector<double>> probs(stages, std::vector<double>(MA, 0.0));

    // Stage 0: For a 4-sided die, outcomes 1-4 have equal probability.
    probs[0][1] = 1.0 / 4;
    probs[0][2] = 1.0 / 4;
    probs[0][3] = 1.0 / 4;
    probs[0][4] = 1.0 / 4;

    int m_sum = 4;  // Maximum sum possible at stage 0.

    // Loop over remaining stages (i = 1, 2, 3) corresponding to 6-, 8-, and 12-sided dice.
    for (size_t i = 1; i < D.size(); i++) {
        cout << "Stage " << i << ", previous m_sum = " << m_sum << "\n";
        int sides = D[i];

        // "ways" holds the evolving probability distribution (starting with a delta at 0).
        std::vector<double> ways(MA, 0.0);
        ways[0] = 1.0;

        // Update the maximum possible sum.
        m_sum *= sides;

        // For each possible previous outcome index (from 1 to m_sum inclusive)
        // update the distribution for the current stage.
        for (int last_sum = 1; last_sum <= m_sum; last_sum++) {
            std::vector<double> new_ways(MA, 0.0);

            // Convolve the current distribution with one additional dice roll.
            for (int k = 0; k < m_sum; k++) {
                for (int s = 1; s <= sides; s++) {
                    if (k + s >= MA)
                        continue;
                    new_ways[k + s] += ways[k];
                }
            }
            // Normalize new_ways.
            double S = std::accumulate(new_ways.begin(), new_ways.end(), 0.0);
            if (S != 0.0) {
                for (size_t q = 0; q < new_ways.size(); q++) {
                    new_ways[q] /= S;
                }
            }
            // Update the probability distribution for this stage
            // weighted by the probability from the previous stage.
            for (int q = 0; q < MA; q++) {
                probs[i][q] += probs[i - 1][last_sum] * new_ways[q];
            }
            // Prepare for the next iteration.
            ways = new_ways;
        }
    }

    // Normalize the final stage probability distribution.
    double S_total = std::accumulate(probs[stages - 1].begin(), probs[stages - 1].end(), 0.0);
    if (S_total != 0.0) {
        for (int i = 0; i < MA; i++) {
            probs[stages - 1][i] /= S_total;
        }
    }

    double EV_sq = 0.0;
    double EV = 0.0;
    for (int i = 1; i <= MA; i++) {
        EV += probs[stages - 1][i] * i;
        EV_sq += probs[stages - 1][i] * (i * i);
    }
    cout << setprecision(20) << fixed << "ACTUAL EV: " << EV << ", Var: " << (EV_sq - EV * EV) << "\n";

    return 0;
}
