import urllib.request as url_req
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

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = url_req.urlopen(graph_url)
    graph_text = graph_file.read().decode("utf-8")
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    print("Loaded graph with", len(graph_lines), "nodes")

    result_dict = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        result_dict[node] = set([])
        for neighbor in neighbors[1: -1]:
            result_dict[node].add(int(neighbor))

    return result_dict

# ----------------------------------------
citation_graph = load_graph(CITATION_URL)
norm = normalize_distribution(citation_graph)

mplot.loglog([float(k) for k in norm.keys()], [float(v) for v in norm.values()], linestyle = "None", marker = ".")
mplot.title("LOG-LOG Plot of: \nIn-degrees vs Normalized In-degrees")
mplot.ylabel("log(Normalized In-degrees)")
mplot.xlabel("log(In-degrees)")
mplot.savefig("Log-Log Plot of In-degrees vs Normalized In-degrees.png")
mplot.show()
