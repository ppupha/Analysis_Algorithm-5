#include "string_search.h"

int standart(const std::string &str, const std::string &substr) {
    const auto str_len = str.length();
    const auto sub_len = substr.length();

    for (size_t i = 0; i <= str_len - sub_len; i++) {
        auto tmp_i = i;
        for (size_t j = 0; j < sub_len; j++) {
            if (substr[j] != str[tmp_i]) {
                break;
            }
            if (j == sub_len - 1) {
                return static_cast<int>(i);
            }
            tmp_i++;
        }
    }

    return -1;
}

std::vector<size_t> get_shift(const std::string &str, const size_t &size) {
    std::vector<size_t> shift(size);
    shift[0] = 0;

    for (size_t i = 1; i < size; i++) {
        size_t j = shift[i - 1];
        while (j > 0 && str[i] != str[j]) {
            j = shift[j - 1];
        }
        if (str[i] == str[j]) {
            j++;
        }
        shift[i] = j;
    }

    return shift;
}

int kmp(std::string str, std::string substr) {
    auto str_len = str.length();
    auto sub_len = substr.length();
    if (str_len < sub_len) {
        return -1;
    }

    std::vector<size_t> shift = get_shift(substr, sub_len);

    for (size_t j = 0, i = 0; i < str_len; i++) {
        while (j > 0 && str[i] != substr[j]) {
            j = shift[j - 1];
        }
        if (str[i] == substr[j]) {
            j++;
        }
        if (j == sub_len) {
            return static_cast<int>(i - j + 1);
        }
    }

    return -1;
}

std::map<char, size_t> get_shift(const std::string &substr) {
    size_t alphabet_size = 256;
    auto sub_size = substr.length();
    std::map<char, size_t> shift;

    for (size_t symb = 0; symb < alphabet_size; ++symb) {
        shift[static_cast<char>(symb)] = sub_size;
    }

    for (size_t symb = 0; symb < sub_size - 1; ++symb) {
        shift[static_cast<char>(substr[symb])] = sub_size - symb - 1;
    }

    return shift;
}

int bm(std::string str, std::string substr) {
    auto str_len = str.length();
    auto sub_len = substr.length();
    if (str_len < sub_len) {
        return -1;
    }

    auto shift = get_shift(substr);
    auto start = sub_len - 1;
    auto i = start;
    auto j = start;
    auto k = start;

    while (j >= 0 && i < str_len) {
        j = start;
        k = i;
        while (j >= 0 && str[k] == substr[j]) {
            --k;
            --j;
        }

        i += shift[str[i]];
    }

    return static_cast<int>(k >= str_len - sub_len ? -1 : k + 1);
}