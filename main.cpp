#include <iostream>
#include <cmath>
#include <fstream>

int main(int argc, char* argv[]) {
    double primary_base = std::stod(argv[1]);
    double secondary_base = std::stod(argv[2]);
    unsigned long length = std::stoul(argv[3]);
    if (argc != 4 or primary_base < 2 or secondary_base < 2 or length == 0 or length > 18446700000000000000) {
        std::cout << argc << '\n';
        std::cout << argv[1] << '\n';
        std::cout << argv[2] << '\n';
        std::cout << argv[3] << '\n';
        return 1;
    }
    else {
        std::ofstream radix_average("radix_average.txt", std::ios::trunc);
        double total = 0;
        unsigned long i_last = 0;
        for (unsigned long i = 1; i <= length;) {
            double y = (double) (i - i_last) * primary_base / secondary_base * (floor(log((double) i) / log(primary_base) + 1) / floor(log((double) i) / log(secondary_base) + 1));
            total += y;
            radix_average << total / (double) i << ',' << i << '\n';
            i_last = i;
            i += (long) std::max(1.0, pow(10, ceil(log10((double) i + 1)) - 1) / 100000);
        }
        return 0;
    }
}