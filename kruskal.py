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
            

def min_tree(graph):
    edges = sorted(graph.edges(data=True), key=lambda t: t[2].get('weight', 1))
    tree = nx.Graph()
    tree.add_nodes_from(graph)
    edges_in_tree = []
    nodes_in_tree = len(graph.nodes)
    while len(edges_in_tree) < nodes_in_tree - 1:
        for edge in edges:
            tree.add_edge(edge[0], edge[1], weight=edge[2]['weight'])
            if  check_cycle(tree, edge[0]) == True:
                tree.remove_edge(edge[0], edge[1])              
            else:
                edges_in_tree.append(edge)
                continue
    
    return tree
        
    
    
    
        
    
node = 10
graph = rand_graph(node)
tree = min_tree(graph)
print(len(graph.edges))
print(len(tree.edges))
pos = nx.spring_layout(graph)
fig = plt.figure()
nx.draw_networkx(graph, pos)
fig.savefig("graph.png")
pos = nx.spring_layout(tree)
fig = plt.figure()
nx.draw_networkx(tree, pos)
fig.savefig("tree.png")
plt.show()