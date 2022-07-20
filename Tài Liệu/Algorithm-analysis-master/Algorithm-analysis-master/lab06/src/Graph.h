#ifndef LAB06_GRAPH_H
#define LAB06_GRAPH_H

#include <algorithm>
#include <vector>
#include <random>

class Graph {
public:
    explicit Graph(size_t vertices_number);
    Graph(size_t vertices_number, float init_value);

    static Graph generate_graph(size_t size, int noise);

    void addPath(size_t vertex_from, size_t vertex_to, int length);
    void set(size_t i, size_t j, float value);
    float get(size_t i, size_t j) const;
    size_t size() const;
    std::vector<size_t> getAvailableVertexes(size_t vertex, const std::vector<size_t> &taboo_list) const;
private:
    std::vector<std::vector<float>> matrix;
};


#endif //LAB06_GRAPH_H
