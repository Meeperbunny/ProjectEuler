#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// Idea is that we have an id, left bound, right bound for the grundy numbers. We have a set of grundy numbers touched by the 
// 1.0 ptr and the 1.41 ptr. We move: leftmost_rb - ptr_pos to the right, and get rid of the leftmost_rb[id], then insert all new ones we cross.
// Then, we place a grundy number inside the set for what we were. We don't worry about off by one. In the end, we have a good way to calc this.
// So we will have generate

const double r2 = sqrt(2.0);

map<double, bool> genGrundy(double R) {
    // M.lower_bount(i)->second is true iff the first player wins. 
    auto m = map<double, bool>();
    m[0.0] = false;
    m[r2] = true;
    m[2.0 + r2] = false;
}

int main() {
    double L = 4;

    return 0;
}