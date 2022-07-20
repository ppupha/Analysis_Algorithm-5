// Lab_01_AA.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
#include <iomanip>
#include "levenshtein_dist.h"
#include "time.h"



int main() {
    std::string s1, s2;

    std::cout << "Enter 1st string: ";
    std::cin >> s1;
    std::cout << "Enter 2nd string: ";
    std::cin >> s2;

    char time_test;
    std::cout << "Run time test, y/n? ";
    std::cin >> time_test;

    if (time_test == 'y') {
        std::cout << std::endl << "Levenshtein distance (Matrix)" << std::endl;
        std::cout << "Time: " << std::fixed << std::setprecision(8)
            << check_time([&]() { levenshtein(s1, s2); }) << "s" << std::endl << std::endl;
        print_lev_matrix(s1, s2);
        std::cout << std::endl << "Result: " << levenshtein(s1, s2) << std::endl;

        std::cout << std::endl << std::endl << "Levenshtein distance (Recursive)" << std::endl;
        std::cout << "Time: " << std::fixed << std::setprecision(8)
            << check_time([&]() { recursive_levenshtein(s1, s2); }) << "s" << std::endl;
        std::cout << "Result: " << recursive_levenshtein(s1, s2) << std::endl;

        std::cout << std::endl << std::endl << "Damerau-Levenshtein distance (Matrix)" << std::endl;
        std::cout << "Time: " << std::fixed << std::setprecision(8)
            << check_time([&]() { dam_lev_dist(s1, s2); }) << "s" << std::endl << std::endl;
        print_dam_lev_matrix(s1, s2);
        std::cout << std::endl << "Result: " << dam_lev_dist(s1, s2);
    }
    else {
        std::cout << std::endl << "Levenshtein distance (Matrix)" << std::endl;
        print_lev_matrix(s1, s2);
        std::cout << std::endl << "Result: " << levenshtein(s1, s2) << std::endl;

        std::cout << std::endl << std::endl << "Levenshtein distance (Recursive)" << std::endl;
        std::cout << "Result: " << recursive_levenshtein(s1, s2) << std::endl;

        std::cout << std::endl << std::endl << "Damerau-Levenshtein distance (Matrix)" << std::endl;
        print_dam_lev_matrix(s1, s2);
        std::cout << std::endl << "Result: " << dam_lev_dist(s1, s2);
    }

    return 0;
}

// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
