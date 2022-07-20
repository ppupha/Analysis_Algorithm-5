
#include <string>
#include <iostream>
#include "parallel_vinograd.h"

void test(const std::string &test_name, matrix_d &m1, matrix_d &m2, matrix_d &expected) {
    std::cout << test_name << std::endl;

    for (int i = 1; i < 4; i++) {
        std::cout << "Threads number: " << i << std::endl;
        auto vin_res = parallel_vinograd_mult(m1, m2, 2);
        if (vin_res != expected) {
            std::cout << "vinograd failed" << std::endl;
        } else {
            std::cout << "vinograd passed" << std::endl;
        }
    }
    std::cout << std::endl;
}



int main() {
    auto m1 = matrix_d({row_d{1, 2, 3}, row_d{1, 2, 3}, row_d{1, 2, 3}});
    auto m2 = matrix_d({row_d{1, 2, 3}, row_d{1, 2, 3}, row_d{1, 2, 3}});
    auto expected = matrix_d({row_d{6, 12, 18}, row_d{6, 12, 18}, row_d{6, 12, 18}});
    test("odd matrix size test", m1, m2, expected);

    m1 = matrix_d({row_d{1, 2}, row_d{1, 2}});
    m2 = matrix_d({row_d{1, 2}, row_d{1, 2}});
    expected = matrix_d({row_d{3, 6}, row_d{3, 6}});
    test("even matrix size test", m1, m2, expected);

    m1 = matrix_d({row_d{2}});
    m2 = matrix_d({row_d{2}});
    expected = matrix_d({row_d{4}});
    test("one element matrix test", m1, m2, expected);

    m1 = matrix_d({row_d{1, -2, 3}, row_d{1, 2, 3}, row_d{1, 2, 3}});
    m2 = matrix_d({row_d{-1, 2, 3}, row_d{1, 2, 3}, row_d{1, 2, 3}});
    expected = matrix_d({row_d{0, 4, 6}, row_d{4, 12, 18}, row_d{4, 12, 18}});
    test("matrix with negative elements test", m1, m2, expected);

    return 0;
}