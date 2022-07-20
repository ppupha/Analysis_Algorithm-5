#ifndef LAB06_ANT_ALGORITHM_H
#define LAB06_ANT_ALGORITHM_H

#include <random>
#include "Graph.h"

struct Parameters {
    float a;
    float b;
    float p;
    float q;
    float start_pheromone;
    size_t times;
};

struct SimulationResult {
    std::vector<size_t> path;
    size_t days;
    float path_len;
};

class Colony {
public:
    explicit Colony(Graph &graph);
    SimulationResult simulation(Parameters parameters, size_t days);
private:
    static constexpr const float START_PHEROMONE = 0.3f;

    std::default_random_engine generator;
    std::uniform_real_distribution<float> distribution = std::uniform_real_distribution<float>(0, 1);

    Graph _graph;
    Graph _pheromone_graph;
    Parameters _parameters;

    std::pair<std::vector<size_t>, float> antAlgorithm(size_t start_vert);
    float random_probability();
    std::vector<float> vertexes_probabilities(size_t curr_vertex, const std::vector<size_t> &available_vertexes);
    size_t chose_vert(size_t vertex, const std::vector<size_t> &taboo_list);
    void update_pheromone(const std::vector<std::vector<size_t>> &paths);
};

#endif //LAB06_ANT_ALGORITHM_H
