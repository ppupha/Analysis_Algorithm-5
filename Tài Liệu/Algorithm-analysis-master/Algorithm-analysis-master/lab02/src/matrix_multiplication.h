#ifndef MATRIX_MULTIPLICATION
#define MATRIX_MULTIPLICATION

#include <vector>
using matrix_d = std::vector<std::vector<double>>;
using row_d = std::vector<double>;

matrix_d init_matrix(size_t n, size_t m);
matrix_d common_multiplication(matrix_d &m1, matrix_d &m2);
row_d get_negative_row_products(matrix_d &matrix, size_t m, size_t n);
row_d get_negative_col_products(matrix_d &matrix, size_t m, size_t n);
matrix_d vinograd_multiplication(matrix_d &m1, matrix_d &m2);
row_d bad_get_negative_row_products(matrix_d &matrix, size_t m, size_t n);
row_d bad_get_negative_col_products(matrix_d &matrix, size_t m, size_t n);
matrix_d bad_vinograd_multiplication(matrix_d &m1, matrix_d &m2);

#endif //MATRIX_MULTIPLICATION
