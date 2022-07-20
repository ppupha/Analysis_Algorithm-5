#include "parallel_vinograd.h"

row_d parallel_negative_row_products(matrix_d &matrix, size_t m, size_t n, size_t threads_num) {
    auto result = row_d(m, 0.);
    auto lambda = [&](size_t i_start, size_t i_end) {
        for (size_t i = i_start; i < i_end; i++) {
            for (size_t j = 0; j < n - 1; j += 2) {
                result[i] -= matrix[i][j] * matrix[i][j + 1];
            }
        }
    };

    std::vector<std::thread> threads(threads_num);
    auto line_for_thread = m / threads_num;
    if (line_for_thread == 0) {
        line_for_thread = 1;
    }

    for (size_t i = 0; i < threads_num && i < m; i++) {
        size_t start = i * line_for_thread;
        size_t end = i == threads_num - 1? m: (i + 1) * line_for_thread;
        auto thread = std::thread(lambda, start, end);
        threads[i] = std::move(thread);
    }

    for (auto &thr: threads) {
        thr.join();
    }

    return result;
}

row_d parallel_negative_col_products(matrix_d &matrix, size_t m, size_t n, size_t threads_num) {
    auto result = row_d(m, 0.);
    auto lambda = [&](size_t i_start, size_t i_end) {
        for (size_t i = i_start; i < i_end; i++) {
            for (size_t j = 0; j < n - 1; j += 2) {
                result[i] -= matrix[j][i] * matrix[j + 1][i];
            }
        }
    };

    std::vector<std::thread> threads(threads_num);
    auto line_for_thread = m / threads_num;
    if (line_for_thread == 0) {
        line_for_thread = 1;
    }

    for (size_t i = 0; i < threads_num && i < m; i++) {
        size_t start = i * line_for_thread;
        size_t end = i == threads_num - 1? m: (i + 1) * line_for_thread;
        auto thread = std::thread(lambda, start, end);
        threads[i] = std::move(thread);
    }

    for (auto &thr: threads) {
        if (thr.joinable()) {
            thr.join();
        }
    }

    return result;
}

matrix_d parallel_vinograd_mult(matrix_d &m1, matrix_d &m2, size_t threads_num) {
    auto l = m1.size();
    auto m = m2.size();
    auto n = m2[0].size();

    if (m1[0].size() != m) {
        throw std::exception();
    }

    row_d mh, mv;
    if (threads_num > 2) {
        std::thread mh_thread([&](){ mh = get_negative_row_products(m1, l, m); });
        std::thread mv_thread([&](){ mv = get_negative_col_products(m2, n, m); });
        mh_thread.join();
        mv_thread.join();
    } else {
        mh = parallel_negative_row_products(m1, l, m, threads_num / 2);
        mv = parallel_negative_col_products(m2, n, m, threads_num - threads_num / 2);
    }

    std::vector<std::thread> threads(threads_num);
    auto line_for_thread = l / threads_num;
    if (line_for_thread == 0) {
        line_for_thread = 1;
    }

    auto result = init_matrix(l, n);
    for (size_t i = 0; i < threads_num && i < l; i++) {
        size_t start = i * line_for_thread;
        size_t end = i == threads_num - 1? l: (i + 1) * line_for_thread;
        auto thread = std::thread(
            [&](size_t i_start, size_t i_end) {
                for (size_t local_i = i_start; local_i < i_end; local_i++) {
                    for (size_t j = 0; j < m; j++) {
                        result[local_i][j] = mh[local_i] + mv[j];
                        for (size_t k = 0; k < n-1; k += 2) {
                            result[local_i][j] += (m1[local_i][k + 1] + m2[k][j]) * (m1[local_i][k] + m2[k + 1][j]);
                        }
                    }
                }
            }, start, end);
        threads[i] = std::move(thread);
    }

    for (auto &thr: threads) {
        if (thr.joinable()) {
            thr.join();
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