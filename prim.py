# Generate a minimum spanning tree using Prim's algorithm on a randomly generated tree.
from cProfile import Profile
from pstats import Stats
import sys
prof = Profile()

prof.disable()

import networkx as nx
import matplotlib.pyplot as plt
import random
from queue import PriorityQueue
plt.rcParams['figure.figsize'] = [10, 10]

#Generate a random, connected graph with randomly weighted edges
def rand_graph(node):
    g = nx.Graph()
    for i in range(0, node): # Add n nodes to graph
        g.add_node(i)
    for j in range(1, node): # Ensure that there are no disconnected nodes
        g.add_edge(j-1, i, weight=random.randint(10, 20))
    for k in range(node * 5): # Add a bunch more edges, just for funsies
        g.add_edge(random.randint(0, node), random.randint(0, node), weight = random.randint(10, 20))
    g.remove_edges_from(nx.selfloop_edges(g)) # Remove any self-loops in the graph
    return g

# Generate a minimal tree using a priority queue to sort edge data from the original graph
def min_tree(graph, node):
    edges_in_tree = set()
    nodes_in_tree = set()
    queue = PriorityQueue()
    start = random.randint(0, node-1) # Arbitrarily chosen starting node
    for neighbor in graph.neighbors(start): # Add all neighboring edges of start to queue
        edge_data = graph.get_edge_data(start, neighbor)
        edge_weight = edge_data['weight']
        queue.put((edge_weight, (start, neighbor))) 
    while len(nodes_in_tree) < node: 
        _, edge = queue.get(queue)
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
    
node = 10
seed = 0.5
graph = rand_graph(node)
prof.enable()
tree = min_tree(graph, node)
prof.disable()
prof.dump_stats("prim.stats")
with open('prim-output.txt', 'a') as output:
    output.write("Test:  # of nodes-  " + str(node) + ". \n")
    stats = Stats('prim.stats', stream=output)
    stats.sort_stats('time')
    stats.print_stats()
    
    
pos = nx.spring_layout(graph)
fig = plt.figure()
nx.draw_networkx(graph, pos)
fig.savefig("primgraph.png")
pos = nx.spring_layout(tree)
fig = plt.figure()
nx.draw_networkx(tree, pos)
fig.savefig("primtree.png")
plt.show()
