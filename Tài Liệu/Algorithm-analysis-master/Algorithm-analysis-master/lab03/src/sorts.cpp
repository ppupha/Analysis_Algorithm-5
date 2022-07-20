#include "sorts.h"

void bubble_sort(std::vector<double> &arr) {
    if (arr.empty()) {
        return;
    }

    for (int i = 0; i < arr.size() - 1; i++) {
        for (int j = 1; j < arr.size(); j++) {
            if (arr[j] < arr[j - 1]) {
                std::swap(arr[j - 1], arr[j]);
            }
        }
    }
}

void insertion_sort(std::vector<double> &arr) {
    if (arr.empty()) {
        return;
    }

    for (size_t i = 1; i < arr.size(); i++) {
        auto cur_item = arr[i];
        int j = static_cast<int>(i - 1);
        for (; j >= 0 && arr[j] > cur_item; j--) {
            arr[j + 1] = arr[j];
        }
        arr[j + 1] = cur_item;
    }
}

void choice_sort(std::vector<double> &arr) {
    if (arr.empty()) {
        return;
    }

    for (size_t i = 0; i < arr.size() - 1; i++) {
        auto min_ind = i;
        for (size_t j = i + 1; j < arr.size(); j++) {
            if (arr[j] < arr[min_ind]) {
                min_ind = j;
            }
        }
        std::swap(arr[min_ind], arr[i]);
    }
}
