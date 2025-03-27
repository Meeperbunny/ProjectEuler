from fractions import Fraction

# Define the dice sides for each stage: d4, d6, d8, d12.
D = [4, 6, 8, 12]

# MA is used to size the arrays; it is the product of all dice sides plus one.
MA = 1
for e in D:
    MA *= e
MA += 1

# Initialize the probability distribution for stage 0 (the d4 roll).
# Only outcomes 1,2,3,4 are possible, each with probability 1/4.
probs = [[Fraction(0) for _ in range(MA)] for _ in range(len(D))]
probs[0][1] = Fraction(1, 4)
probs[0][2] = Fraction(1, 4)
probs[0][3] = Fraction(1, 4)
probs[0][4] = Fraction(1, 4)

m_sum = 4  # maximum sum for stage 0 (d4) is 4

# For each subsequent stage, update the probability distribution.
# The idea is: the number of dice to roll in the next stage equals the outcome
# from the previous stage. We perform a convolution of distributions accordingly.
for i in range(1, len(D)):
    print(f"Stage {i}, current m_sum = {m_sum}")
    sides = D[i]
    # Start with a distribution 'ways' where only 0 has probability 1.
    ways = [Fraction(0) for _ in range(MA)]
    ways[0] = Fraction(1)
    
    # Update the maximum sum possible.
    m_sum *= D[i]
    
    # For each possible previous outcome (number of dice to roll),
    # compute the distribution for the sum when rolling that many dice.
    for last_sum in range(1, m_sum + 1):
        # Compute convolution for one extra dice roll stage.
        new_ways = [Fraction(0) for _ in range(MA)]
        for k in range(0, m_sum):
            # Skip if there is no way to get sum 'k' in this intermediate step.
            if ways[k] == 0:
                continue
            # Add outcomes for rolling one die with "sides" sides.
            for s in range(1, sides + 1):
                if k + s >= MA:
                    continue
                new_ways[k + s] += ways[k]
        # Normalize new_ways to get a probability distribution.
        S = sum(new_ways)
        if S != 0:
            for q in range(MA):
                new_ways[q] = new_ways[q] / S
        # Weight by the probability of having 'last_sum' from the previous stage.
        for q in range(MA):
            probs[i][q] += probs[i - 1][last_sum] * new_ways[q]
        # Prepare for the next iteration.
        ways = new_ways.copy()

# Normalize the final probability distribution to ensure it sums to 1.
S_total = sum(probs[len(D) - 1])
for i in range(MA):
    if S_total != 0:
        probs[len(D) - 1][i] = probs[len(D) - 1][i] / S_total

# Compute the expected value (EV) of the final distribution.
EV = Fraction(0)
for i in range(MA):
    EV += i * probs[len(D) - 1][i]

print("Expected value from the multi-stage dice rolls (exact):", EV)

# --- Now, incorporate the final d20 stage analytically ---

# Compute the variance of a d20 roll exactly.
# The variance of a fair n-sided die (with sides 1..n) is given by: Var = (n^2 - 1)/12.
# For n = 20, this is:
v_20 = Fraction(20**2 - 1, 12)
# The expected value of a d20 is (n+1)/2.
ev_20 = Fraction(21, 2)

print("Variance of a d20 (exact):", v_20)
print("Expected value of a d20 (exact):", ev_20)

# Now, compute the overall expected value and variance after multiplying
# each outcome by the expected value of a d20 (for the final stage).
EV_multiplied = Fraction(0)
EV_sq_multiplied = Fraction(0)
for i in range(1, MA):
    # The final stage result is i * (average of d20)
    outcome = i * ev_20
    EV_multiplied += probs[len(D) - 1][i] * outcome
    EV_sq_multiplied += probs[len(D) - 1][i] * outcome**2

variance_multiplied = EV_sq_multiplied - EV_multiplied**2

print("Overall expected value after multiplying by d20 average (exact):", EV_multiplied)
print("Overall variance after multiplying by d20 average (exact):", variance_multiplied)
