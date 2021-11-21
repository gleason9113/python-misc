# Generate a minimum spanning tree using Prim's algorithm on a randomly generated tree.
from cProfile import Profile
from pstats import Stats
import sys
prof = Profile()

prof.disable()

import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations as combos
import random
from queue import PriorityQueue
plt.rcParams['figure.figsize'] = [10, 10]


#Generate a graph from the provided text file
def rand_graph(city_set):
    file = open("city-pairs.txt")
    city_list = file.readlines()   
    g = nx.Graph()
    for pair in city_list:
        parts = pair.split(' ')
        city_set.add(parts[0])
        city_set.add(parts[1])
    g.add_nodes_from(city_set)
    for pair in city_list:
        parts = pair.split(' ')
        g.add_edge(parts[0], parts[1], weight=parts[2])
    return g

# Generate a minimal tree using a priority queue to sort edge data from the original graph
def min_tree(graph, city_set):
    node = len(city_set)
    edges_in_tree = set()
    nodes_in_tree = set()
    queue = PriorityQueue()
    start = random.choice(list(city_set)) # Arbitrarily chosen starting node
    for neighbor in graph.neighbors(start): # Add all neighboring edges of start to queue
        edge_data = graph.get_edge_data(start, neighbor)
        edge_weight = edge_data['weight']
        queue.put((edge_weight, (start, neighbor))) 
    while len(nodes_in_tree) < node: 
        i, edge = queue.get(queue)
        if edge[0] not in nodes_in_tree: # Check whether either node of edge is missing from set
            n_node = edge[0]
        elif edge[1] not in nodes_in_tree: # Add if missing
            n_node = edge[1]
        else:
            continue # Otherwise move to the next edge in the queue
        for neighbor in graph.neighbors(n_node): # For the newly added node, add all neighbors to queue
            edge_data = graph.get_edge_data(n_node, neighbor)
            edge_weight = edge_data['weight']
            queue.put((edge_weight, (n_node, neighbor)))
        edges_in_tree.add(tuple(sorted(edge))) # Add edges and nodes to the sets
        nodes_in_tree.add(n_node)
    tree = nx.Graph()
    tree.add_nodes_from(nodes_in_tree)
    tree.add_edges_from(edges_in_tree)
    return tree


city_set = set()
graph = rand_graph(city_set)
prof.enable()
tree = min_tree(graph, city_set)
prof.disable()
prof.dump_stats("primt.stats")
with open('primt.txt', 'a') as output:
    stats = Stats('primt.stats', stream=output)
    stats.sort_stats('time')
    stats.print_stats()
pos = nx.spring_layout(graph)
fig = plt.figure()
nx.draw_networkx(graph, pos)
fig.savefig("citygraph.png")
pos = nx.spring_layout(tree)
fig = plt.figure()
nx.draw_networkx(tree, pos)
fig.savefig("citytree.png")
plt.show()
