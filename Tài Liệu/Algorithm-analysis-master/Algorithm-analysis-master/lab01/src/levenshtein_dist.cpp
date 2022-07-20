#include <vector>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include "levenshtein_dist.h"

int recursive_lev(std::string str1, std::string str2) {
    auto len1 = str1.length();
    auto len2 = str2.length();

    if (len1 == 0) {
        return static_cast<int>(len2);
    }
    if (len2 == 0) {
        return static_cast<int>(len1);
    }

    auto last_symb = str1[len1 - 1] == str2[len2 - 1]? 0: 1;

    auto s1 = std::string(str1, 0, len1 - 1);
    auto s2 = std::string(str2, 0, len2 - 1);

    return std::min( { recursive_lev(str1, s2) + 1,
                       recursive_lev(s1, str2) + 1,
                       recursive_lev(s1, s2) + last_symb });
}

int lev(std::string str1, std::string str2) {
    std::vector<int> a1(str2.length() + 1);
    std::vector<int> a2(str2.length() + 1);
    // initialisation of 1st row
    for (int i = 0; i < a1.size(); i++) a1[i] = i;

    for (int i = 1; i < str1.length() + 1; i++) {
        a2.at(0) = a1.at(0) + 1;
        for (int j = 1; j < str2.length() + 1; j++) {
            auto vertical = a1[j] + 1;
            auto horisontal = a2[j - 1] + 1;
            auto diagonal = a1[j - 1] + (str1[i - 1] == str2[j - 1]? 0: 1);
            a2[j] = std::min({ vertical, horisontal, diagonal });
        }
        std::copy(a2.begin(), a2.end(), a1.begin());
    }
    a2.at(0) = -1;
    return a2.at(a2.size() - 1);
}


// It's not in lev function to measure time of algorithm work
void print_lev_matrix(std::string str1, std::string str2) {
    std::vector<int> a1(str2.length() + 1);
    std::vector<int> a2(str2.length() + 1);
    // initialisation of 1st row
    for (int i = 0; i < a1.size(); i++) a1[i] = i;

    std::cout << "Matrix:" << std::endl;
    std::cout << "       λ";
    for (auto c: str2) std::cout << std::setw(4) << c;
    std::cout << std::endl;

    for (int i = 1; i < str1.length() + 1; i++) {
        a2[0] = a1[0] + 1;
        for (int j = 1; j < str2.length() + 1; j++) {
            auto vertical = a1[j] + 1;
            auto horisontal = a2[j - 1] + 1;
            auto diagonal = a1[j - 1] + (str1[i - 1] == str2[j - 1]? 0: 1);
            a2[j] = std::min({ vertical, horisontal, diagonal });
        }
        if (i == 1) {
            std::cout << std::setw(5) << "λ";
        } else {
            std::cout << std::setw(4) << str1[i - 2];
        }
        for (int item : a1) {
            std::cout << std::setw(4)<< item;
        }
        std::cout << std::endl;

        a1 = a2;
    }
    std::cout << std::setw(4) << str1[str1.length() - 1];
    for (int item : a2) {
        std::cout << std::setw(4) << item;
    }
    std::cout << std::endl;
}

int dam_lev_dist(std::string str1, std::string str2) {
    std::vector<int> a0(str2.length() + 1);
    std::vector<int> a1(str2.length() + 1);
    std::vector<int> a2(str2.length() + 1);
    // initialisation of 1st row
    for (int i = 0; i < a1.size(); i++) a1[i] = i;

    for (int i = 1; i < str1.length() + 1; i++) {
        a2[0] = a1[0] + 1;
        for (int j = 1; j < str2.length() + 1; j++) {
            auto eq = str1[i - 1] == str2[j - 1]? 0: 1;

            auto vertical = a1[j] + 1;
            auto horisontal = a2[j - 1] + 1;
            auto diagonal = a1[j - 1] + eq;
            a2[j] = std::min({ vertical, horisontal, diagonal });

            // swap
            if (i && j && str1[i - 1] == str2[j - 2] && str1[i - 2] == str2[j - 1]) {
                a2[j] = std::min(a2[j], a0[j - 2] + eq);
            }
        }
        a0 = a1;
        a1 = a2;
    }

    return a2[a2.size() - 1];
}

// It's not in dam_lev_dist function to measure time of algorithm work
void print_dam_lev_matrix(std::string str1, std::string str2) {
    std::vector<int> a0(str2.length() + 1);
    std::vector<int> a1(str2.length() + 1);
    std::vector<int> a2(str2.length() + 1);
    // initialisation of 1st row
    for (int i = 0; i < a1.size(); i++) a1[i] = i;

    std::cout << "Matrix:" << std::endl;
    std::cout << "       λ";
    for (auto c: str2) std::cout << std::setw(4) << c;
    std::cout << std::endl;

    for (int i = 1; i < str1.length() + 1; i++) {
        a2[0] = a1[0] + 1;
        for (int j = 1; j < str2.length() + 1; j++) {
            auto eq = str1[i - 1] == str2[j - 1]? 0: 1;

            auto vertical = a1[j] + 1;
            auto horisontal = a2[j - 1] + 1;
            auto diagonal = a1[j - 1] + eq;
            a2[j] = std::min({ vertical, horisontal, diagonal });

            // swap
            if (i && j && str1[i - 1] == str2[j - 2] && str1[i - 2] == str2[j - 1]) {
                a2[j] = std::min(a2[j], a0[j - 2] + eq);
            }
        }
        if (i == 1) {
            std::cout << std::setw(5) << "λ";
        } else {
            std::cout << std::setw(4) << str1[i - 1];
        }
        for (int item : a1) {
            std::cout << std::setw(4) << item;
        }
        std::cout << std::endl;
        a0 = a1;
        a1 = a2;
    }
    std::cout << std::setw(4) << str2[str2.length() - 1];
    for (int item : a2) {
        std::cout << std::setw(4) << item;
    }
    std::cout << std::endl;
}