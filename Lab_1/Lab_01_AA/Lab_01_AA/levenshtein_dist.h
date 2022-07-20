#ifndef LAB01_LEVENSHTEIN_DIST_H
#define LAB01_LEVENSHTEIN_DIST_H

#include <string>

int recursive_levenshtein(std::string str1, std::string str2);
void print_lev_matrix(std::string str1, std::string str2);
int levenshtein(std::string str1, std::string str2);
void print_dam_lev_matrix(std::string str1, std::string str2);
int dam_lev_dist(std::string str1, std::string str2);

#endif //LAB01_LEVENSHTEIN_DIST_H
