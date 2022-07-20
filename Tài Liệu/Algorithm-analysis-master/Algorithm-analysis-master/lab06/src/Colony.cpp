#include <algorithm>
#include "Colony.h"

Colony::Colony(Graph &graph)
    : _graph(graph), _pheromone_graph(graph.size(), START_PHEROMONE) {}

std::pair<std::vector<size_t>, float> Colony::antAlgorithm(size_t start_vert) {
    std::vector<size_t> taboo_list = {start_vert};

    auto current_vertex = start_vert;
    while (taboo_list.size() != _graph.size()) {
        current_vertex = chose_vert(current_vertex, taboo_list);
        taboo_list.push_back(current_vertex);
    }

    auto len = 0.f;
    for (size_t i = 0; i < taboo_list.size(); i++) {
        if (i < taboo_list.size() - 1) {
            len += _graph.get(taboo_list.at(i), taboo_list.at(i + 1));
        }
        else {
            len += _graph.get(taboo_list.at(i), taboo_list.at(0));
        }
    }

    return std::make_pair(taboo_list, len);
}

void Colony::update_pheromone(const std::vector<std::vector<size_t>> &paths) {
    for (size_t i = 0; i < _graph.size(); i++) {
        for (size_t j = 0; j < _graph.size(); j++) {
            if (i == j) {
                continue;
            }

            _pheromone_graph.set(i, j, _pheromone_graph.get(i, j) * (1 - _parameters.p));
            if (_pheromone_graph.get(i, j) <= 1e-5) {
                _pheromone_graph.set(i, j, 0.3);
            }
        }
    }

    for (auto &path: paths) {
        for (size_t i = 0; i < path.size(); i++) {
            size_t from = 0, to = 0;
            if (i != path.size() - 1) {
                from = path.at(i);
                to = path.at(i + 1);
            }
            else {
                from = path.at(i);
                to = path.at(0);
            }

            auto delta = _parameters.q / _graph.get(from, to);
            auto new_val = _pheromone_graph.get(from, to) + delta;
            _pheromone_graph.set(from, to, new_val);
            _pheromone_graph.set(to, from, new_val);
        }
    }
}

float Colony::random_probability() {
    return distribution(generator);
}

size_t Colony::chose_vert(size_t vertex, const std::vector<size_t> &taboo_list) {
    auto probability = random_probability();
    auto available_vertexes = _graph.getAvailableVertexes(vertex, taboo_list);

    auto probabilities = vertexes_probabilities(vertex, available_vertexes);
    auto denominator = std::accumulate(probabilities.begin(), probabilities.end(), 0.f);

    auto curr_prob = 0.f;
    for (auto &v: available_vertexes) {
        curr_prob += probabilities.at(v) / denominator;
        if (probability <= curr_prob) {
            return v;
        }
    }

    return available_vertexes[available_vertexes.size() - 1];
}

std::vector<float> Colony::vertexes_probabilities(size_t curr_vertex, const std::vector<size_t> &available_vertexes) {
    std::vector<float> probabilities(_graph.size(), 0);

    for (auto &v: available_vertexes) {
        probabilities.at(v) = static_cast<float &&>(
            std::pow(_pheromone_graph.get(curr_vertex, v), _parameters.a)
                * std::pow(1. / _graph.get(curr_vertex, v), _parameters.b)
        );
    }

    return probabilities;
}

SimulationResult Colony::simulation(Parameters parameters, size_t days) {
    _pheromone_graph = Graph(_graph.size(), START_PHEROMONE);
    std::vector<size_t> best_path;
    float best_path_len = -1;
    _parameters = parameters;
    size_t days_to_find = 0;

    for (size_t i = 0; i < days; i++) {
        std::vector<std::vector<size_t>> day_paths(_graph.size());
        for (size_t v = 0; v < _graph.size(); v++) {
            auto result = antAlgorithm(v);
            day_paths.at(v) = result.first;

            if (best_path_len == -1 || result.second < best_path_len) {
                best_path = result.first;
                best_path_len = result.second;
                days_to_find = i + 1;
            }
        }
        update_pheromone(day_paths);
    }

    return {best_path, days_to_find, best_path_len};
}

