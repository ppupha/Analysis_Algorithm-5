#ifndef LAB06_EXHAUSTIVE_SEARCH_H
#define LAB06_EXHAUSTIVE_SEARCH_H

#include <vector>
#include "Graph.h"

using Path = std::vector<size_t>;

float path_len(const Graph &graph, const Path &path);
std::pair<Path, float> exhaustive_search(const Graph &graph);

#endif //LAB06_EXHAUSTIVE_SEARCH_H
