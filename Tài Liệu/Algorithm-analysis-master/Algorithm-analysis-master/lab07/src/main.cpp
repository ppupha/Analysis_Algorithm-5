#include <iostream>
#include <vector>

#include "string_search.h"

using namespace std;

int main() {
    string  str;
    string substr;

    cout << "Enter string: ";
    cin >> str;
    cout << "Enter substring: ";
    cin >> substr;

    auto res = standart(str, substr);
    cout << "Standart algorithm result: " << res << endl;

    res = kmp(str, substr);
    cout << "KMP algorithm result: " << res << endl;

    res = bm(str, substr);
    cout << "BM algorithm result: " << res << endl;

    return 0;
}