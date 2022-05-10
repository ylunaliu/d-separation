from platform import node
import networkx as nx
import numpy as np
import itertools
from checkdseparation import check_d_separation_total

def d_separation_list(graph):
    nodes = np.array(graph.nodes)
    # Now we have a way to check if given two nodes and a set z, we need all cominbination of two nodes and set z and store it to a table
    def adjustformat(nodes):
        nodes_adjust_format = ''
        for node in nodes:
            nodes_adjust_format = nodes_adjust_format + node
        return(nodes_adjust_format)
    nodes_adjust_format = adjustformat(nodes)

    # Get all combination of two nodes
    combination = list(itertools.combinations(nodes_adjust_format,2))

    # Get all combibation for set Z
    def powerset(input):
        output = sum([list(map(list, itertools.combinations(input, i))) for i in range(len(input) + 1)], [])
        return output
    # Get all the nodes:
    sets_z = powerset(nodes)

    for i in range(len(combination)):
        for j in range(len(sets_z)):
            if(check_d_separation_total(graph, combination[i], sets_z[j])==True):
                print(f'{combination[i][0]} and {combination[i][1]} are d-separated by {sets_z[j]}')
            else:
                print(f'{combination[i][0]} and {combination[i][1]} are not d-separated by {sets_z[j]}')

if __name__ == "__main__":
   # graph = nx.DiGraph()
   # graph.add_edges_from([("x", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
    # descendants = list(nx.descendants(graph,"a"))
    # print(descendants)
    # z = ["h"]
    # print(set(descendants).isdisjoint(z))

    graph1 = nx.DiGraph()
    graph1.add_edges_from([("s", "a"), ("l", "a"), ("l", "b"), ("t", "b")])
    d_separation_list(graph1)