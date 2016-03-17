"""
A simple graph interface:
"""

"""
# Constants ----------------------------------------------------------------------------------------------------------

Constants used for testing

EX_GRAPH0 = {0: {1, 2}, 1: set(), 2: set()}
EX_GRAPH1 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3}, 3: {0}, 4: {1}, 5: {2}, 6: set()}
EX_GRAPH2 = {0: {1, 4, 5}, 1: {2, 6}, 2: {3, 7}, 3: {7}, 4: {1}, 5: {2}, 6: set(),
             7: {3}, 8: {1, 2}, 9: {0, 4, 5, 6, 7, 3}}
"""
# Public Methods -----------------------------------------------------------------------------------------------------
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

