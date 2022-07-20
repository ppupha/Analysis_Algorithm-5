#include <ctime>
#include <random>
#include <functional>
#include <iostream>
#include <iomanip>
#include "matrix_multiplication.h"

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
    int n = 1;
    clock_t start = clock();
    for (int i = 0; i < n; i++) {
        f();
    }
    clock_t end = clock();
    return static_cast<double >(end - start) / CLOCKS_PER_SEC / n;
}

int main() {
    srand(unsigned(std::time(nullptr)));

    for (size_t i = 100; i <= 1000; i+= 100) {
        auto matrix1 = generate_matrix(i);
        auto matrix2 = generate_matrix(i);

        std::cout << "Matrix size: " << i << std::endl;
        std::cout << "Common algorithm time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ common_multiplication(matrix1, matrix2); }) << "s" << std::endl << std::endl;
        std::cout << "Bad Vinograd's algorithm time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ bad_vinograd_multiplication(matrix1, matrix2); }) << "s" << std::endl << std::endl;
        std::cout << "Vinograd's algorithm time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ vinograd_multiplication(matrix1, matrix2); }) << "s" << std::endl << std::endl;
        std::cout << std::endl;
    }

    for (size_t i = 101; i <= 1001; i+= 100) {
        auto matrix1 = generate_matrix(i);
        auto matrix2 = generate_matrix(i);

        std::cout << "Matrix size: " << i << std::endl;
        std::cout << "Common algorithm time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ common_multiplication(matrix1, matrix2); }) << "s" << std::endl << std::endl;
        std::cout << "Bad Vinograd's algorithm time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ bad_vinograd_multiplication(matrix1, matrix2); }) << "s" << std::endl << std::endl;
        std::cout << "Vinograd's algorithm time: " << std::fixed << std::setprecision(8)
                  << check_time( [&](){ vinograd_multiplication(matrix1, matrix2); }) << "s" << std::endl << std::endl;
        std::cout << std::endl;
    }

    return 0;
}
