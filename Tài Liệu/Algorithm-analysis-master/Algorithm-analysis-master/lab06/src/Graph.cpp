#include <chrono>
#include "Graph.h"

Graph::Graph(size_t vertices_number) {
    matrix.resize(vertices_number);
    for (auto &row: matrix) {
        row = std::vector<float>(vertices_number, -1);
    }
}

void Graph::addPath(size_t vertex_from, size_t vertex_to, int length) {
    matrix.at(vertex_from).at(vertex_to) = length;
}

std::vector<size_t> Graph::getAvailableVertexes(size_t vertex, const std::vector<size_t> &taboo_list) const {
    std::vector<size_t > result;
    for (size_t i = 0; i < matrix.size(); i++) {
        if (matrix.at(vertex).at(i) > 0 and std::find(taboo_list.begin(), taboo_list.end(), i) == taboo_list.end()) {
            result.push_back(i);
        }
    }
    return result;
}

void Graph::set(size_t i, size_t j, float value) {
    matrix.at(i).at(j) = value;
}

float Graph::get(size_t i, size_t j) const {
    return matrix.at(i).at(j);
}

size_t Graph::size() const {
    return matrix.size();
}

Graph::Graph(size_t vertices_number, float init_value) {
    matrix.resize(vertices_number);
    for (auto &row: matrix) {
        row = std::vector<float>(vertices_number, init_value);
    }
}

Graph Graph::generate_graph(size_t size, int noise) {
    std::default_random_engine generator(static_cast<unsigned long>(std::chrono::steady_clock::now().time_since_epoch().count()));
    std::uniform_int_distribution<int> distribution(1, noise);

    Graph graph(size);
    for (size_t i = 0; i < size; ++i) {
        for (size_t j = 0; j < size; ++j) {
            graph.set(i, j, distribution(generator));
        }
    }

    return graph;
}
