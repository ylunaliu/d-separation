from platform import node
import networkx as nx
import numpy as np
import itertools
from checkdseparation import check_d_separation_total
from toolz import unique

def d_separation_list(graph, hidden_nodes):
    # Graph is a directed graph object
    # hidden_nodes is a list contains the hidden variables in the from ["a", "b" ...]
    nodes = list(graph.nodes)
    
    if(hidden_nodes!=[]):
        for node in hidden_nodes:
            nodes.remove(node)

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
        # Now I get a pair of nodes I can regenerate the powerset for the nodes
        new_nodes = make_z_not_overlap_with_nodes(list(combination[i]), list(nodes))
        sets_z = powerset(new_nodes)
        for j in range(len(sets_z)):
            if(check_d_separation_total(graph, combination[i], sets_z[j])==True):
                    print(f'{combination[i][0]} and {combination[i][1]} are d-separated by {sets_z[j]}')



def make_z_not_overlap_with_nodes(pair, sets_z):
    new_set = sets_z
    for element in pair:
        if element in new_set:
            new_set.remove(element)

    return new_set

if __name__ == "__main__":
   # graph = nx.DiGraph()
   # graph.add_edges_from([("x", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
    # descendants = list(nx.descendants(graph,"a"))
    # print(descendants)
    # z = ["h"]
    # print(set(descendants).isdisjoint(z))

    # Need to define the 11 graphs
    # #2 Bell's seno
    # graph_2 = nx.DiGraph()
    # graph_2.add_edges_from([("B", "E"), ("A", "E"), ("A", "D"), ("C", "D")])
    # graph_2_hidden = list(["A"])
    # print("The d-separation for graph 2 is")
    # d_separation_list(graph_2,graph_2_hidden)

#     The d-separation for graph 2 is
#     B and D are d-separated by []
#     B and D are d-separated by ['C']
#     B and C are d-separated by []
#     B and C are d-separated by ['E']
#     B and C are d-separated by ['D']
#     E and C are d-separated by []
#     E and C are d-separated by ['B']

    # #3 Unrelated confounder
    # graph_3 = nx.DiGraph()
    # graph_3.add_edges_from([("A", "E"), ("C", "E"), ("C", "D"), ("A", "C"), ("B", "C"), ("B", "D")])
    # graph_3_hidden = list(["A", "B"])
    # d_separation_list(graph_3,graph_3_hidden)

#     The d-separation for graph 3 is
#     None

    # # Graph 1
    # graph_1 = nx.DiGraph()
    # graph_1.add_edges_from([("A", "D"), ("A", "C"),("C", "D"), ("B", "C")])
    # graph_1_hidden = list(["A"])
    # d_separation_list(graph_1, graph_1_hidden)

#     The d-separation for graph 1 is
#     None


    # Graph 4
    # graph_4 = nx.DiGraph()
    # graph_4.add_edges_from([("A", "F"), ("A", "C"), ("B", "C"), ("B", "E"), ("D", "E"), ("C", "F"), ("E", "F")])
    # graph_4_hidden = list(["A", "B"])
    # d_separation_list(graph_4, graph_4_hidden)

#     The d-separation for graph 4 is
#     C and D are d-separated by []


    # Graph 5 
    # graph_5 = nx.DiGraph()
    # graph_5.add_edges_from([("A", "E"), ("A", "F"), ("E", "F"), ("B", "F"), ("B", "D"), ("D", "E"), ("C", "D")])
    # graph_5_hidden = list(["A", "B"])
    # d_separation_list(graph_5, graph_5_hidden)

#     The d-separation for graph 5 is
#     E and C are d-separated by ['D']


    # Graph 16
    # graph_16 = nx.DiGraph()
    # graph_16.add_edges_from([("A", "E"), ("A", "F"), ("B", "F"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")])
    # graph_16_hidden = list(["A", "B"])
    # d_separation_list(graph_16, graph_16_hidden)

#     The d-separation for graph 16 is
#     F and C are d-separated by []
    
    
    # Graph 17
    # graph_17 = nx.DiGraph()
    # graph_17.add_edges_from([("A", "F"), ("A", "C"), ("B", "C"), ("B", "E"), ("D", "E"), ("C", "F"), ("C", "E"), ("E", "F")])
    # graph_17_hidden = list(["A", "B"])
    # d_separation_list(graph_17, graph_17_hidden)

#    The d-separation for graph 17 is
#    C and D are d-separated by []


    # Graph 18

    # graph_18 = nx.DiGraph()
    # graph_18.add_edges_from([("A", "F"), ("A", "D"), ("B", "D"), ("B", "E"), ("D", "E"), ("C", "D"), ("C", "E"), ("E", "F")])
    # graph_18_hidden = list(["A", "C"])
    # d_separation_list(graph_18, graph_18_hidden)

#     The d-separation for graph 18 is
#     None

    # Graph 19

    # graph_19 = nx.DiGraph()
    # graph_19.add_edges_from([("A", "F"), ("A", "D"), ("B", "C"), ("B", "E"), ("D", "E"), ("C", "D"), ("C", "E"), ("E", "F")])
    # graph_19_hidden = list(["A", "C"])
    # d_separation_list(graph_19, graph_19_hidden)

#     The d-separation for graph 19 is
#     None


    # Graph 20
    graph_20 = nx.DiGraph()
    graph_20.add_edges_from([("A", "E"), ("A", "F"), ("B", "F"), ("B", "D"), ("C", "D"), ("D", "E")])
    graph_20_hidden = list(["A", "B"])
    d_separation_list(graph_20, graph_20_hidden)

#   E and C are d-separated by ['D']
#   F and C are d-separated by []

    # graph1 = nx.DiGraph()
    # graph1.add_edges_from([("s", "a"), ("l", "a"), ("l", "b"), ("t", "b")])
    # print(graph1.nodes)
    # hidden_nodes = ["b"]
    # d_separation_list(graph1, hidden_nodes)



