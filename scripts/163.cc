#include <iostream>
#include <cmath>
#include <vector>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <sstream>
#include <iomanip>

// Use our own definition of PI.
const double PI = 3.14159265358979323846;
// Global constant.
const double x_const = 1.0;

// Round a double to 'decimals' places.
double roundTo(double value, int decimals) {
    double factor = std::pow(10.0, decimals);
    return std::round(value * factor) / factor;
}

// Rounded tangent: tan(angle) rounded to 3 decimals.
double tanRounded(double angle) {
    return roundTo(std::tan(angle), 3);
}

// A point is defined by its coordinates and a label.
struct Point {
    double x, y;
    std::string label;
};

// For use in sets to filter duplicate (rounded) coordinates.
struct Coord {
    double x, y;
    bool operator<(const Coord &other) const {
        if (std::fabs(x - other.x) > 1e-9)
            return x < other.x;
        return y < other.y;
    }
};

// Allowed slopes per label.
// For vertical lines we “store” a None in Python but here we simply omit it,
// since verticality is handled separately.
std::unordered_map<std::string, std::vector<double>> AXIS_SLOPES = {
    {"CO", {0.0, tanRounded(PI/6), tanRounded(PI/3), tanRounded(2*PI/3), tanRounded(5*PI/6)}},
    {"C",  {tanRounded(PI/6), tanRounded(5*PI/6)}},
    {"TR", {tanRounded(PI/6), tanRounded(2*PI/3)}},
    {"BO", {0.0}},
    {"TL", {tanRounded(5*PI/6), tanRounded(PI/3)}}
};

// are_same_axis: returns true if two points share an allowed axis.
// If the x–difference is nearly zero (vertical), we return true if b’s label is one
// of "CO", "C", or "BO". Otherwise we compute the slope and check against a's allowed slopes.
bool are_same_axis(const Point &a, const Point &b) {
    if (std::fabs(a.x - b.x) < 1e-3) {
        return (b.label == "CO" || b.label == "C" || b.label == "BO");
    }
    double slope = (a.y - b.y) / (a.x - b.x);
    double angle = std::atan(slope);
    double tan_val = roundTo(std::tan(angle), 3);
    auto it = AXIS_SLOPES.find(a.label);
    if (it != AXIS_SLOPES.end()) {
        for (double allowed : it->second) {
            if (std::fabs(allowed - tan_val) < 1e-3)
                return true;
        }
    }
    return false;
}

// is_degenerate_triangle: returns true if the triangle defined by points a, b, c is degenerate
// (i.e. two points coincide or the area is nearly zero).
bool is_degenerate_triangle(const Point &a, const Point &b, const Point &c, double tol = 1e-6) {
    if ((std::fabs(a.x - b.x) < 1e-9 && std::fabs(a.y - b.y) < 1e-9) ||
        (std::fabs(b.x - c.x) < 1e-9 && std::fabs(b.y - c.y) < 1e-9) ||
        (std::fabs(a.x - c.x) < 1e-9 && std::fabs(a.y - c.y) < 1e-9))
        return true;
    double area = std::fabs(a.x*(b.y - c.y) + b.x*(c.y - a.y) + c.x*(a.y - b.y)) / 2.0;
    return area < tol;
}

// gen_triangle: given a center (as a pair) and a flag 'reversed', returns a vector of Points
// corresponding to the triangle (including the center with label "C" and six surrounding points).
std::vector<Point> gen_triangle(const std::pair<double, double>& center, bool reversed) {
    std::vector<Point> pts;
    pts.push_back({center.first, center.second, "C"});
    double R = reversed ? PI : 0.0;
    // Each tuple: (multiplier, angle offset, label)
    std::vector<std::tuple<double, double, std::string>> defs = {
        {1, PI/6,    "TR"},
        {1, 5*PI/6,  "TL"},
        {1, 9*PI/6,  "BO"},
        {2, 3*PI/6,  "CO"},
        {2, 7*PI/6,  "CO"},
        {2, 11*PI/6, "CO"}
    };
    for (auto &def : defs) {
        double mult, offset;
        std::string label;
        std::tie(mult, offset, label) = def;
        double angle = R + offset;
        double pt_x = center.first + mult * x_const * std::cos(angle);
        double pt_y = center.second + mult * x_const * std::sin(angle);
        pts.push_back({pt_x, pt_y, label});
    }
    return pts;
}

// gen_points: generates points arranged in a spiral of triangles.
// Duplicate points (after rounding to 2 decimals) are filtered out.
std::vector<Point> gen_points(int k) {
    std::set<Coord> seen;
    std::vector<Point> points;
    int i = 0, increment = 1, start = 0;
    double base = 0.0;
    while (true) {
        if (i == k - 1)
            increment = -1;
        // Loop over positions in this row: j runs from 1 to i+1.
        for (int j = 1; j <= i + 1; j++) {
            int q = start + j;
            int offset = (j - 1) / 2;
            double radius = 2 * x_const * (2 * start + q + offset);
            double center_x = base + radius * std::cos(PI/6);
            double center_y = radius * std::sin(PI/6);
            std::pair<double, double> center = {center_x, center_y};
            bool reversed = (j % 2 == 0);
            std::vector<Point> tri = gen_triangle(center, reversed);
            for (auto &p : tri) {
                double rx = roundTo(p.x, 2);
                double ry = roundTo(p.y, 2);
                Coord rounded = {rx, ry};
                if (seen.find(rounded) == seen.end()) {
                    seen.insert(rounded);
                    points.push_back(p);
                }
            }
        }
        base -= 2 * x_const * std::sqrt(3);
        i += increment;
        if (increment == -1)
            start++;
        if (i < 0)
            break;
    }
    return points;
}

int main() {
    // Generate our points.
    std::vector<Point> P = gen_points(3);
    int n = P.size();

    // Precompute axis comparisons cache:
    // Create an n x n matrix (only i < j used) storing:
    //   -1: not computed; 0: false; 1: true.
    std::vector<std::vector<int>> axis_cache(n, std::vector<int>(n, -1));
    auto axis_pair = [&](int i, int j) -> bool {
        if (axis_cache[i][j] == -1) {
            bool res = are_same_axis(P[i], P[j]);
            axis_cache[i][j] = res ? 1 : 0;
        }
        return axis_cache[i][j] == 1;
    };

    // Total number of triangle combinations.
    unsigned long long total_combinations = (unsigned long long)n * (n - 1) * (n - 2) / 6;
    unsigned long long progressInterval = total_combinations / 100;
    if (progressInterval == 0) progressInterval = 1;

    // Count valid triangles.
    // A valid triangle is nondegenerate and all three pairs share an allowed axis.
    unsigned long long count = 0;
    unsigned long long iter = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                iter++;
                if (iter % progressInterval == 0) {
                    double progress = (double)iter / total_combinations * 100.0;
                    std::cerr << "\rProgress: " << std::fixed << std::setprecision(6)
                              << progress << "% " << std::flush;
                }
                if (!is_degenerate_triangle(P[i], P[j], P[k]) &&
                    axis_pair(i, j) && axis_pair(i, k) && axis_pair(j, k))
                {
                    count++;
                }
            }
        }
    }
    std::cerr << "\rProgress: 100.00% " << std::endl;
    std::cout << count << std::endl;
    return 0;
}
