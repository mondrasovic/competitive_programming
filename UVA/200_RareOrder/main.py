import collections
import itertools
import sys


def iter_test_cases():
    lines = []
    for line in filter(
        lambda l: len(l) > 0, map(str.strip, sys.stdin.readlines())
    ):
        if '#' in line:
            yield lines
            lines.clear()
        else:
            lines.append(line)


def build_letter_precedence_graph(word_list):
    letter_graph = {}
    
    def _init(letter):
        if letter not in letter_graph:
            letter_graph[letter] = set()
    
    if len(word_list) == 1:
        _init(word_list[0][0])
    else:
        for word_1, word_2 in itertools.combinations(word_list, 2):
            for letter_1, letter_2 in zip(word_1, word_2):
                _init(letter_1)
                _init(letter_2)

                if letter_1 != letter_2:
                    letter_graph[letter_1].add(letter_2)
                    break
    
    return letter_graph


def topological_sort(graph):
    dfs_nodes = collections.deque()
    visited = set()

    def _dfs_visit(node):
        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                _dfs_visit(neighbor)
            
            dfs_nodes.appendleft(node)
    
    for node in graph.keys():
        _dfs_visit(node)
    
    return dfs_nodes


def find_collating_seq(letter_graph):
    dfs_nodes = topological_sort(letter_graph)
    collating_seq = ''.join(dfs_nodes)
    return collating_seq


for word_list in iter_test_cases():
    letter_graph = build_letter_precedence_graph(word_list)
    print(find_collating_seq(letter_graph))
