from platform import node
import networkx as nx
import numpy as np
import itertools


def check_d_separation_total(graph, pair, z):
    edges = graph.edges
    graph2 = nx.Graph()
    graph2.add_edges_from(edges)
    #pair is a list containg two nodes ['a', 'b']
    #z is a set of variable containing a set of nodes ["a"]

    #Create all the paths between the two nodes
    paths = list(nx.all_simple_paths(graph2, pair[0], pair[1]))
    is_d_separate_path = []
    # Preliminary check if there exits a path that's unblockable
    if(preliminary_check(paths) == False):
        return False
    else:
        for path in paths:
            adjecent_nodes = create_list_adjencent_nodes(path)
            property_list = create_list_property(adjecent_nodes, edges)
            is_d_separate = check_d_separation(property_list, adjecent_nodes, z, graph)
            is_d_separate_path.append(is_d_separate)

        # Need to be true for all the 
        if not False in is_d_separate_path:
            return True
        else:
            return False


def preliminary_check(paths):
    for path in paths:
        if len(path) == 2:
            return False
        else:
            return True

def create_list_adjencent_nodes(path):
    adjecent_nodes = []
    for i in range(len(path)-2):
        adjecent_nodes.append(path[i:i+3])
    return adjecent_nodes


def check_property(adjecent_node, edges):
    # the input is a list with three nodes ['a', 'b', 'c'], it will check if it is a fork, chain or collider
    node1 = (adjecent_node[0], adjecent_node[1])
    node2 = (adjecent_node[1], adjecent_node[2])
    dir1 = node1 in edges
    dir2 = node2 in edges

    if(dir1 and dir2):
        return "chain"
    if(dir1 and ~dir2):
        return "collider"
    if(~dir1 and ~dir2):
        return "fork"

def create_list_property(adjecent_nodes, edges):
    property_list = []
    for i in range(len(adjecent_nodes)):
        property_list.append(check_property(adjecent_nodes[i], edges))
    return property_list


def check_d_separation(property_list, adjecent_nodes, z, graph):
    # adjecent_nodes have the all the adjecent_nodes in the graph
    # property_list is a list contain if the combination if a chain, fork, or collider
    is_d_separate_list = []
    for i in range(len(property_list)):
        if(property_list[i] == "chain"):
            is_separate = adjecent_nodes[i][1] in z
        if(property_list[i]=="fork"):
            is_separate = adjecent_nodes[i][1] in z
        if(property_list[i]=="collider"):
            # Need to add the descendent check
            is_separate =  adjecent_nodes[i][1] not in z and set(list(nx.descendants(graph,adjecent_nodes[i][1]))).isdisjoint(z)
        is_d_separate_list.append(is_separate)
        
    if True in is_d_separate_list:
        return True
    else:
        return False
    
if __name__ == "__main__":
    # graph = nx.DiGraph()
    # graph.add_edges_from([("x", "a"), ("a", "b"), ("a", "e"), ("b", "c"), ("b", "d"), ("d", "e")])
    # pair = ["x", "d"]
    graph1 = nx.DiGraph()
    graph1.add_edges_from([("s", "a"), ("l", "a"), ("l", "b"), ("t", "b")])
    graph2 = nx.Graph()
    graph2.add_edges_from(graph1.edges)
  
    pair = ["a", "b"]
    print(check_d_separation_total(graph1, pair, []))
