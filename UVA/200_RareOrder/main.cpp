#include <vector>
#include <string>
#include <stack>
#include <sstream>
#include <unordered_map>
#include <iostream>
#include <algorithm>
#include <unordered_set>

using namespace std;

typedef unordered_map<char, unordered_set<char>> graph_t;

static const int kLettersNum = 26;

static void dfs_visit(
    char node, const graph_t& graph, vector<bool> *visited,
    stack<char>* dfs_nodes)
{
    auto node_val = node - 'A';

    if (!(*visited)[node_val]) {
        (*visited)[node_val] = true;

        for (const auto& neighbor : graph.at(node)) {
            dfs_visit(neighbor, graph, visited, dfs_nodes);
        }

        dfs_nodes->push(node);
    }
}

static void find_collating_seq(const graph_t &graph, string *seq)
{
    stack<char> dfs_nodes;
    vector<bool> visited(kLettersNum, false);

    for (const auto& item : graph) {
        dfs_visit(item.first, graph, &visited, &dfs_nodes);
    }

    stringstream ss;
    while (!dfs_nodes.empty()) {
        ss << dfs_nodes.top();
        dfs_nodes.pop();
    }

    *seq = ss.str();
}

static void build_letter_precedence_graph(
    const vector<string>& word_list, graph_t *graph) {
    if (word_list.size() == 1) {
        graph->insert({word_list[0][0], unordered_set<char>()});
    } else {
        for (size_t i = 0; i < word_list.size() - 1; ++i) {
            const auto& word_1(word_list[i]);

            for (size_t j = i + 1; j < word_list.size(); ++j) {
                const auto& word_2(word_list[j]);
                auto common_len = min(word_1.size(), word_2.size());

                for (size_t k = 0; k < common_len; ++k) {
                    auto letter_1(word_1[k]);
                    auto letter_2(word_2[k]);

                    if (graph->count(letter_1) == 0) {
                        graph->insert({letter_1, unordered_set<char>()});
                    }

                    if (graph->count(letter_2) == 0) {
                        graph->insert({letter_2, unordered_set<char>()});
                    }

                    if (letter_1 != letter_2) {
                        graph->at(letter_1).emplace(letter_2);
                        break;
                    }
                }
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    string word;
    vector<string> word_list;
    while (getline(cin, word)) {
        if (word[0] == '#') {
            graph_t graph;
            string seq;

            build_letter_precedence_graph(word_list, &graph);
            find_collating_seq(graph, &seq);
            cout << seq << endl;

            word_list.clear();
        } else {
            word_list.emplace_back(word);
        }
    }

    return 0;
}
