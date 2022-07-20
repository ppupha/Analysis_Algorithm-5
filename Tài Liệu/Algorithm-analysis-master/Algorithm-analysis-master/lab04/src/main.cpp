#include <ctime>
#include <random>
#include <functional>
#include <iostream>
#include <iomanip>
#include "parallel_vinograd.h"

matrix_d generate_matrix(size_t size) {
    auto m = init_matrix(size, size);

    for (size_t i = 0; i < size; i++) {
        for (size_t j = 0; j < size; j++) {
            m[i][j] = rand() % 2000 - 1000;
        }
    }

    return m;
}

double check_time(const std::function<void()> &f) {
    int n = 10;
    std::chrono::time_point<std::chrono::system_clock> start, end;
    start = std::chrono::system_clock::now();
    for (int i = 0; i < n; i++) {
        f();
    }
    end = std::chrono::system_clock::now();
    return double(std::chrono::duration_cast<std::chrono::nanoseconds>(end-start).count()) / 1e9;
}

int main() {
    srand(unsigned(std::time(nullptr)));

    for (size_t i = 700; i <= 1000; i+= 100) {
        size_t thread_number = 2;
        auto matrix1 = generate_matrix(i);
        auto matrix2 = generate_matrix(i);

        std::cout << "Matrix size: " << i << std::endl;
        for (; thread_number <= 64; thread_number *= 2) {
            std::cout << "Threads: " << thread_number << std::endl;
            std::cout << "Parallel algorithm time: " << std::fixed << std::setprecision(8)
                      << check_time([&]() { parallel_vinograd_mult(matrix1, matrix2, thread_number); }) << "s"
                      << std::endl;
        }
        std::cout << "Not parallel algorithm time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ vinograd_multiplication(matrix1, matrix2); }) << "s" << std::endl << std::endl;
        std::cout << std::endl;
    }

    for (size_t i = 101; i <= 1001; i+= 100) {
        size_t thread_number = 2;
        auto matrix1 = generate_matrix(i);
        auto matrix2 = generate_matrix(i);

        std::cout << "Matrix size: " << i << std::endl;
        for (; thread_number <= 64; thread_number *= 2) {
            std::cout << "Threads: " << thread_number << std::endl;
            std::cout << "Parallel algorithm time: " << std::fixed << std::setprecision(8)
                      << check_time([&]() { parallel_vinograd_mult(matrix1, matrix2, thread_number); }) << "s"
                      << std::endl;
        }
        std::cout << "Not parallel algorithm time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ vinograd_multiplication(matrix1, matrix2); }) << "s" << std::endl << std::endl;
        std::cout << std::endl;
    }

    return 0;
}
