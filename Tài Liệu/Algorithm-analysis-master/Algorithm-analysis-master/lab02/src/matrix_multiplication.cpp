#include "matrix_multiplication.h"


matrix_d init_matrix(size_t n, size_t m) {
    matrix_d matrix(n);
    for (auto &row: matrix) {
        row = row_d(m, 0.);
    }
    return matrix;
}

matrix_d common_multiplication(matrix_d &m1, matrix_d &m2) {
    auto l = m1.size();
    auto m = m2.size();
    auto n = m2[0].size();

    if (m1[0].size() != m) {
        throw std::exception();
    }

    auto result = init_matrix(l, n);

    for (size_t i = 0; i < l; i++) {
        for (size_t j = 0; j < n; j++) {
            for (int k = 0; k < m; k++) {
                result[i][j] += m1[i][k] * m2[k][j];
            }
        }
    }

    return result;
}

row_d bad_get_negative_row_products(matrix_d &matrix, size_t m, size_t n) {
    auto result = row_d(m, 0.);
    for (size_t i = 0; i < m; i++) {
        for (size_t j = 0; j < n / 2; j++) {
            result[i] = result[i] + matrix[i][j * 2] * matrix[i][j * 2 + 1];
        }
    }

    return result;
}

row_d bad_get_negative_col_products(matrix_d &matrix, size_t m, size_t n) {
    auto result = row_d(m, 0.);
    for (size_t i = 0; i < m; i++) {
        for (size_t j = 0; j < n / 2; j += 2) {
            result[i] = result[i] + matrix[2 * j][i] * matrix[2 * j + 1][i];
        }
    }

    return result;
}

matrix_d bad_vinograd_multiplication(matrix_d &m1, matrix_d &m2) {
    auto l = m1.size();
    auto m = m2.size();
    auto n = m2[0].size();

    if (m1[0].size() != m) {
        throw std::exception();
    }

    auto mh = bad_get_negative_row_products(m1, l, m);
    auto mv = bad_get_negative_col_products(m2, n, m);

    auto result = init_matrix(l, n);
    for (size_t i = 0; i < l; i++) {
        for (size_t j = 0; j < m; j++) {
            result[i][j] = -mh[i] - mv[j];
            for (size_t k = 0; k < n / 2; k++) {
                result[i][j] = result[i][j] + (m1[i][2 * k + 1] + m2[2 * k][j]) * (m1[i][2 * k] + m2[2 * k + 1][j]);
            }
        }
    }

    if (n % 2 == 1) {
        for (size_t i = 0; i < l; i++) {
            for (size_t j = 0; j < m; j++) {
                result[i][j] = result[i][j] + m1[i][n - 1] * m2[n-1][j];
            }
        }
    }

    return result;
}

row_d get_negative_row_products(matrix_d &matrix, size_t m, size_t n) {
    auto result = row_d(m, 0.);
    for (size_t i = 0; i < m; i++) {
        for (size_t j = 0; j < n - 1; j += 2) {
            result[i] -= matrix[i][j] * matrix[i][j + 1];
        }
    }

    return result;
}

row_d get_negative_col_products(matrix_d &matrix, size_t m, size_t n) {
    auto result = row_d(m, 0.);
    for (size_t i = 0; i < m; i++) {
        for (size_t j = 0; j < n - 1; j += 2) {
            result[i] -= matrix[j][i] * matrix[j + 1][i];
        }
    }

    return result;
}

matrix_d vinograd_multiplication(matrix_d &m1, matrix_d &m2) {
    auto l = m1.size();
    auto m = m2.size();
    auto n = m2[0].size();

    if (m1[0].size() != m) {
        throw std::exception();
    }

    auto mh = get_negative_row_products(m1, l, m);
    auto mv = get_negative_col_products(m2, n, m);

    auto result = init_matrix(l, n);
    for (size_t i = 0; i < l; i++) {
        for (size_t j = 0; j < m; j++) {
            result[i][j] = mh[i] + mv[j];
            for (size_t k = 0; k < n - 1; k += 2) {
                result[i][j] += (m1[i][k + 1] + m2[k][j]) * (m1[i][k] + m2[k + 1][j]);
            }
        }
    }

    if (n % 2 == 1) {
        for (size_t i = 0; i < l; i++) {
            for (size_t j = 0; j < m; j++) {
                result[i][j] += m1[i][n - 1] * m2[n-1][j];
            }
        }
    }

    return result;
}