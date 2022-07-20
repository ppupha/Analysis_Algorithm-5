#include <string>
#include <iostream>
#include "matrix_multiplication.h"

void test(const std::string &test_name, matrix_d &m1, matrix_d &m2, matrix_d &expected) {
    std::cout << test_name << std::endl;
    auto com_res = common_multiplication(m1, m2);
    if (com_res != expected) {
        std::cout << "common failed" << std::endl;
    } else {
        std::cout << "common passed" << std::endl;
    }

    auto bad_vin_res = vinograd_multiplication(m1, m2);
    if (bad_vin_res != expected) {
        std::cout << "bad vinograd failed" << std::endl;
    } else {
        std::cout << "bad vinograd passed" << std::endl;
    }
    
    auto vin_res = vinograd_multiplication(m1, m2);
    if (vin_res != expected) {
        std::cout << "vinograd failed" << std::endl;
    } else {
        std::cout << "vinograd passed" << std::endl;
    }
}



int main() {
    auto m1 = matrix_d({row_d{1., 2., 3.}, row_d{1, 2, 3}, row_d{1, 2, 3}});
    auto m2 = matrix_d({row_d{1., 2., 3.}, row_d{1, 2, 3}, row_d{1, 2, 3}});
    auto expected = matrix_d({row_d{6, 12., 18}, row_d{6, 12, 18}, row_d{6, 12, 18}});
    test("1st test", m1, m2, expected);

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