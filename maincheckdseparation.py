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

    # Get all combination of two nodes
    combination = list(itertools.combinations(nodes,2))

    # Get all combibation for set Z
    def powerset(input):
        output = sum([list(map(list, itertools.combinations(input, i))) for i in range(len(input) + 1)], [])
        return output
    # Get all the nodes:
    for i in range(len(combination)):
        # Now I get a pair of nodes I can regenerate the powerset for the nodes
        new_nodes = remove_element_list(list(combination[i]), list(nodes))
        sets_z = powerset(new_nodes)
        for j in range(len(sets_z)):
            if(check_d_separation_total(graph, combination[i], sets_z[j])==True):
                    print(f'{combination[i][0]} and {combination[i][1]} are d-separated by {sets_z[j]}')



def remove_element_list(list1, list2):
    new_sets = list(set(list2).difference(list1))
    return new_sets


def make_z_not_overlap_with_nodes(pair, sets_z):
    new_set = sets_z
    for element in pair:
        if element in new_set:
            new_set.remove(element)

    return new_set

if __name__ == "__main__":

    sprial_inflation = nx.DiGraph()
    sprial_inflation.add_edges_from([("X2", "C2"), ("Z2", "B2"), ("Y2", "A2"),
                                ("X1", "A2"), ("X1", "A1"), ("X1", "C1"), 
                                ("Y1", "A1"), ("Y1", "B1"), ("Y1", "B2"), 
                                ("Z1", "C1"), ("Z1", "B1"), ("Z1", "C2")])
    sprial_inflation_hidden = list(["X2", "Y2", "Z2", "X1", "Y1", "Z1"])

    d_separation_list(sprial_inflation, sprial_inflation_hidden)