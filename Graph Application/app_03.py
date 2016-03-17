from numpy import *
import matplotlib.pyplot as mplot
"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm

    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities

    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a
        complete graph with num_nodes nodes

        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]

    def get_num_nodes(self):
        return self._num_nodes

    def get_node_numbers(self):
        return self._node_numbers


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers

        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities

        Returns:
        Set of nodes
        """

        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))

        # update the list of node numbers so that each node number
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))

        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

def make_complete_graph(num_nodes):
    """
    Creates a complete directed graph

    Arguments:
    num_nodes(int): the number of nodes used to create the graph

    Returns:
    graph(dictionary): dictionary representation of complete directed graph
    """

    graph = {}
    for node in range(num_nodes):
        # start at first node
        adjacent_nodes = set()
        # create an empty set of adjacent nodes that corresponds to current node
        for adj_node in range(num_nodes):
            # find all adjacent nodes
            if adj_node != node:
                adjacent_nodes.add(adj_node)
                # add adjacent node to set
        graph[node] = adjacent_nodes
        # add adjacent note set to dictionary

    return graph

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


def DPA_alg(n, m):
    DPA_obj = DPATrial(m)
    print(DPA_obj.get_num_nodes())

    result = make_complete_graph(m)
    print(result)

    for i in range(m, n):
        node_neighbors = DPA_obj.run_trial(m)
        for j in node_neighbors:
            result[i] = node_neighbors

    return result



graph = DPA_alg(27700, 100)

norm = normalize_distribution(graph)

mplot.loglog([float(k) for k in norm.keys()], [float(v) for v in norm.values()], linestyle = "None", marker = ".")
mplot.title("LOG-LOG Plot of: \nIn-degrees vs Normalized In-degrees (DPA)")
mplot.ylabel("log(Normalized In-degrees)")
mplot.xlabel("log(In-degrees)")
#mplot.savefig("Log-Log Plot of In-degrees vs Normalized In-degrees.png")
mplot.show()