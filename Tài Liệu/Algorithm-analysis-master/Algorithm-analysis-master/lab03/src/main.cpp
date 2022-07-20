#include <functional>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <random>
#include "sorts.h"

using array = std::vector<double>;

double check_time(const std::function<void()> &f) {
    int n = 5;
    clock_t start = clock();
    for (int i = 0; i < n; i++) {
        f();
    }
    clock_t end = clock();
    return static_cast<double >(end - start) / CLOCKS_PER_SEC / n;
}

void init_arrays(array &sorted, array &reversed, array &random) {
    for (int i = 0; i < sorted.size(); i++) {
        sorted[i] = i;
        reversed[reversed.size() - 1 - i] = i;
        random[i] = rand() % 2000 - 1000;
    }
}

void check_sort_time(const array &s, const array &r, const array &random_arr) {
    array sorted(s.size());
    array reversed(r.size());
    array randomised(random_arr.size());

    auto run_check = [&](const std::string &sort_name, const std::function<void(array&)> &sort){
        std::copy(s.begin(), s.end(), sorted.begin());
        std::copy(r.begin(), r.end(), reversed.begin());
        std::copy(random_arr.begin(), random_arr.end(), randomised.begin());
        std::cout << sort_name << std::endl;
        std::cout << "Sorted: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ sort(sorted); }) << "s" << std::endl;
        std::cout << "Reversed: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ sort(reversed); }) << "s" << std::endl;
        std::cout << "Randomised: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ sort(randomised); }) << "s" << std::endl << std::endl;
    };

    run_check("Bubble", bubble_sort);
    run_check("Insertion", insertion_sort);
    run_check("Choice", choice_sort);
}

int main() {
    srand(static_cast<unsigned int>(time(nullptr)));
    std::vector<size_t> sizes{10, 50, 100, 500, 1000, 5000, 20000, 50000};

    for (auto i: sizes) {
        array sorted(i);
        array reversed(i);
        array random(i);
        init_arrays(sorted, reversed, random);

        std ::cout << "Number: " << i << std::endl;
        check_sort_time(sorted, reversed, random);
        std::cout << std::endl << std::endl;
    }
}