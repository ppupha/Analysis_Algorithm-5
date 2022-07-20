#include <algorithm>
#include <string>
#include <iostream>
#include "sorts.h"

void test_sort(const std::string &test_name, const std::vector<double> &arr) {
    std::vector<double> array(arr.size());
    std::copy(arr.begin(), arr.end(), array.begin());
    std::vector<double> expected(arr.size());
    std::copy(arr.begin(), arr.end(), expected.begin());
    std::sort(expected.begin(), expected.end());

    std::cout << test_name << std::endl;
    bubble_sort(array);
    if (array != expected) {
        std::cout << "bubble_sort failed" << std::endl;
    } else {
        std::cout << "bubble_sort passed" << std::endl;
    }
    std::copy(arr.begin(), arr.end(), array.begin());

    insertion_sort(array);
    if (array != expected) {
        std::cout << "insertion_sort failed" << std::endl;
    } else {
        std::cout << "insertion_sort passed" << std::endl;
    }
    std::copy(arr.begin(), arr.end(), array.begin());

    choice_sort(array);
    if (array != expected) {
        std::cout << "choice_sort failed" << std::endl;
    } else {
        std::cout << "choice_sort passed" << std::endl;
    }
    std::cout << std::endl;
}

int main() {
    std::vector<double> sorted{1, 2, 3, 4, 5};
    test_sort("sorted array test", sorted);

    std::vector<double> rev_sorted{5, 4, 3, 2, 1, 0};
    test_sort("reversed array test", rev_sorted);

    std::vector<double> not_sorted{5, 6, 2, 1, 4, -2};
    test_sort("unsorted array test", not_sorted);

    std::vector<double> one_el_arr{4};
    test_sort("one element in array test", one_el_arr);

    std::vector<double> empty_arr;
    test_sort("empty array test", empty_arr);
}