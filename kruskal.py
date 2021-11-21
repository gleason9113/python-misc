from cProfile import Profile
from pstats import Stats
import sys
prof = Profile()

prof.disable()

import networkx as nx
import matplotlib.pyplot as plt
import random
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

# Depth first search function for cycles in graph- returns False if no cycles found
def check_cycle(graph, start):
    seen = {}
    predecessors = {}
    queue = [start]
    seen[start] = 0
    cycles = []
    while queue:
        curr = queue.pop()
        level = seen[curr]
        for node in graph.neighbors(curr):
            if node not in seen:
                predecessors[node] = curr
                seen[node] = level + 1
                queue.append(node)
            else:
                if predecessors[curr] == node:
                    continue
                else:
                    return True
    return False
            
# Build minimum spanning tree using Kruskal algorithm
def min_tree(graph):
    edges = sorted(graph.edges(data=True), key=lambda t: t[2].get('weight', 1)) # Get list of edges sorted by weight
    tree = nx.Graph()
    tree.add_nodes_from(graph)
    edges_in_tree = [] # Loop control
    nodes_in_tree = len(graph.nodes)
    while len(edges_in_tree) < nodes_in_tree - 1:
        for edge in edges:
            tree.add_edge(edge[0], edge[1], weight=edge[2]['weight']) # Add edge to tree
            if  check_cycle(tree, edge[0]) == True: # Check for cycle- if found, remove edge
                tree.remove_edge(edge[0], edge[1])              
            else:
                edges_in_tree.append(edge)   
    return tree
        
   
node = 10
graph = rand_graph(node)

prof.enable()
tree = min_tree(graph)
prof.disable()
prof.dump_stats("krus.stats")
with open('krus-output.txt', 'a') as output:
    output.write("Test:  # of nodes-  " + str(node) + ". \n")
    stats = Stats('krus.stats', stream=output)
    stats.sort_stats('time')
    stats.print_stats()
    
pos = nx.spring_layout(graph)
fig = plt.figure()
nx.draw_networkx(graph, pos)
fig.savefig("krusgraph.png")
pos = nx.spring_layout(tree)
fig = plt.figure()
nx.draw_networkx(tree, pos)
fig.savefig("krustree.png")
plt.show()