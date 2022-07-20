#ifndef PARALLEL_VINOGRAD_H
#define PARALLEL_VINOGRAD_H

#include "../lab02/matrix_multiplication.h"
#include <thread>

row_d parallel_negative_row_products(matrix_d &matrix, size_t m, size_t n, size_t threads_num);
row_d parallel_negative_col_products(matrix_d &matrix, size_t m, size_t n, size_t threads_num);
matrix_d parallel_vinograd_mult(matrix_d &m1, matrix_d &m2, size_t threads_num);

#endif //PARALLEL_VINOGRAD_H
