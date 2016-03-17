from random import uniform
from numpy import *
import matplotlib.pyplot as mplot
"""
Creates a simple log/log plot for a directed graph
"""
EX_GRAPH1 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0}, 4: {1}, 5: {2}, 6: set()}
CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def compute_in_degrees(digraph):
    """
    Computes the number of in-degrees for each node

    Arguments:
    digraph(dictionary): the directed graph being processed

    Returns:
    result_dict(dictionary): new dictionary corresponding to in-degrees of nodes
    """
    result_dict = {}

    for node in digraph:
        # create a dictionary with same nodes as digraph
        result_dict[node] = 0
        # set all nodes to 0

    for node in digraph:
        for adjacent_nodes in digraph[node]:
            result_dict[adjacent_nodes] += 1
            # add 1 for every occurrence of the adjacent node

    return result_dict

def in_degree_distribution(digraph):
    """
    Computes the in-degree distribution for all nodes with at least one edge

    Arguments:
    digraph(dictionary): the directed graph being processed

    Returns:
    result_dict: new dictionary corresponding to the in-degree distribution of nodes
    """

    in_degrees = compute_in_degrees(digraph)
    # first determine the number of in-degrees
    result_dict = dict()

    for node in in_degrees:
        if in_degrees[node] in result_dict:
            # if node IS in new dictionary
            result_dict[in_degrees[node]] += 1
            # add 1 for every occurrence of that particular in-degree
        else:
            # if node is NOT in new dictionary
            result_dict[in_degrees[node]] = 1
            # initialize it and add 1
    return result_dict


def normalize_distribution(digraph):
    dist = in_degree_distribution(digraph)
    result = {}

    size = 0
    for node in dist:
        size += dist[node]

    for node in dist:
        if node != 0:
            result[node] = dist[node] / size

    return result

def ER(num_nodes, p):

    graph = {}
    for node in range(num_nodes):
        # start at first node
        adjacent_nodes = set()
        # create an empty set of adjacent nodes that corresponds to current node
        for adj_node in range(num_nodes):
            # find all adjacent nodes
            a = uniform(0, 1)
            if adj_node != node and a < p:
                adjacent_nodes.add(adj_node)
                # add adjacent node to set
        graph[node] = adjacent_nodes
        # add adjacent note set to dictionary

    return graph

# ----------------------------------------
g = ER(20000, 0.0001)
norm = normalize_distribution(g)

mplot.loglog([float(k) for k in norm.keys()], [float(v) for v in norm.values()], linestyle = "None", marker = ".")
mplot.title("LOG-LOG Plot of: \nIn-degrees vs Normalized In-degrees \nn = 20000, p = 0.0001")
mplot.ylabel("log(Normalized In-degrees)")
mplot.xlabel("log(In-degrees)")
#mplot.savefig("Log-Log Plot of In-degrees vs Normalized In-degrees (ER).png")
mplot.show()