#ifndef LAB07_STRING_SEARCH_H
#define LAB07_STRING_SEARCH_H

#include <string>
#include <vector>
#include <map>

int standart(const std::string &str, const std::string &substr);
int kmp(std::string str, std::string substr);
int bm(std::string str, std::string substr);

#endif //LAB07_STRING_SEARCH_H
