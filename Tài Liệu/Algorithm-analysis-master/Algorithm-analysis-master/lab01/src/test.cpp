#include <iostream>
#include "levenshtein_dist.h"

void test_result(const std::string &s1, const std::string &s2, int exp_result, int exp_resd) {
    int result = recursive_lev(s1, s2);
    if (exp_result != result) {
        std::cout << "recursive_lev failed, s1: " << s1 << ", s2: " << s2 << ", result: " << result << std::endl;
    }

    result = lev(s1, s2);
    if (exp_result != result) {
        std::cout << "lev failed, s1: " << s1 << ", s2: " << s2 << ", result: " << result << std::endl;
    }

    result = dam_lev_dist(s1, s2);
    if (exp_resd != result) {
        std::cout << "dam_lev_dist failed s1: " << s1 << ", s2: " << s2 << "result: " << result << std::endl;
    }
}

int main() {
    test_result("skat", "kot", 2, 2);
    test_result("abc", "abc", 0, 0);
    test_result("abc", "abcdef", 3, 3);
    test_result("abc", "bcde", 3, 3);
    test_result("aaaab", "baaaa", 2, 2);
    test_result("Me", "mE", 2, 2);
    test_result("abc", "acb", 2, 1);

    return 0;
}
