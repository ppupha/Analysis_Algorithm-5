#include <iostream>
#include <functional>
#include <time.h>
#include <iomanip>
#include "levenshtein_dist.h"

double check_time(const std::function<void()> &f) {
    int n = 1;
    clock_t start = clock();
    for (int i = 0; i < n; i++) {
        f();
    }
    clock_t end = clock();
    return static_cast<double >(end - start) / CLOCKS_PER_SEC / n;
}

int main() {
    std::string s1, s2;

    std::cout << "Enter 1st string: ";
    std::cin >> s1;
    std::cout << "Enter 2nd string: ";
    std::cin >> s2;

    char time_test;
    std::cout << "Run time test, y/n? ";
    std::cin >> time_test;

    if (time_test == 'y') {
        std::cout << std::endl << "Levenshtein distance (Matrix)" << std::endl;
        std::cout << "Time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ lev(s1, s2); }) << "s" << std::endl << std::endl;
        print_lev_matrix(s1, s2);
        std::cout << std::endl << "Result: " << lev(s1, s2) << std::endl;

        std::cout << std::endl << std::endl << "Levenshtein distance (Recursive)" << std::endl;
        std::cout << "Time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ recursive_lev(s1, s2); }) << "s" << std::endl;
        std::cout << "Result: " << recursive_lev(s1, s2) << std::endl;

        std::cout << std::endl << std::endl << "Damerau-Levenshtein distance (Matrix)" << std::endl;
        std::cout << "Time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ dam_lev_dist(s1, s2); }) << "s" << std::endl << std::endl;
        print_dam_lev_matrix(s1, s2);
        std::cout << std::endl << "Result: " << dam_lev_dist(s1, s2);
    } else {
        std::cout << std::endl << "Levenshtein distance (Matrix)" << std::endl;
        print_lev_matrix(s1, s2);
        std::cout << std::endl << "Result: " << lev(s1, s2) << std::endl;

        std::cout << std::endl << std::endl << "Levenshtein distance (Recursive)" << std::endl;
        std::cout << "Result: " << recursive_lev(s1, s2) << std::endl;

        std::cout << std::endl << std::endl << "Damerau-Levenshtein distance (Matrix)" << std::endl;
        print_dam_lev_matrix(s1, s2);
        std::cout << std::endl << "Result: " << dam_lev_dist(s1, s2);
    }

    return 0;
}