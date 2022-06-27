#include <iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

typedef unordered_map<int, vector<int>*> graph_t;

static void add_edge(graph_t *graph, int x, int y)
{
    auto neighbors_iter(graph->find(x));
    vector<int> *neighbors;
    if (neighbors_iter == graph->end()) {
        neighbors = new vector<int>();
        graph->insert(make_pair(x, neighbors));
    } else {
        neighbors = neighbors_iter->second;
    }
    neighbors->emplace_back(y);
}

static void find_component(
    int node, const graph_t* graph, vector<int>* nodes,
    unordered_set<int> *visited)
{
    if (visited->count(node) == 0) {
        visited->emplace(node);
        nodes->emplace_back(node);

        for (const auto& neighbor : *graph->at(node)) {
            find_component(neighbor, graph, nodes, visited);
        }
    }
}

static bool is_component_net_zero_sum_possible(
    const graph_t* graph, const vector<int>& node_cost)
{
    unordered_set<int> visited;
    vector<int> component_nodes;

    visited.reserve(graph->size());
    component_nodes.reserve(graph->size());

    for (const auto& item : *graph) {
        component_nodes.clear();
        find_component(item.first, graph, &component_nodes, &visited);

        int component_cost_sum = 0;
        for (const auto& node : component_nodes) {
            component_cost_sum += node_cost[node];
        }

        if (component_cost_sum != 0) {
            return false;
        }
    }

    return true;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n_rem_test_cases;
    cin >> n_rem_test_cases;

    while (--n_rem_test_cases >= 0) {
        int n_people, n_friendships;
        cin >> n_people >> n_friendships;

        vector<int> money_record(n_people, 0);
        for (int i = 0; i < n_people; ++i) {
            cin >> money_record[i];
        }

        graph_t relationship_graph;
        for (int j = 0; j < n_friendships; ++j) {
            int person_x, person_y;
            cin >> person_x >> person_y;

            add_edge(&relationship_graph, person_x, person_y);
            add_edge(&relationship_graph, person_y, person_x);
        }

        auto res = is_component_net_zero_sum_possible(
            &relationship_graph, money_record);
        cout << (res ? "" : "IM") << "POSSIBLE" << endl;

        for (auto item : relationship_graph) {
            delete item.second;
        }
    }

    return 0;
}
