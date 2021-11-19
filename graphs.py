import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations as combos
import random

#Generate a random, connected graph with randomly weighted edges
def rand_graph(node, seed):
    vertices = set([v for v in range(node)])
    edges = set()
    for combo in combos(vertices, 2):
        a = random.random()
        if a < seed:
            edges.add(combo)
    
    g = nx.Graph()
    g.add_nodes_from(vertices)
    g.add_edges_from(edges)
    for edge in g.edges:
        weight = random.randint(0, 10)
        g.edges[edge]['weight'] = weight
    return g
    
node = 10
seed = 0.4
g = rand_graph(node, seed)
pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
# nx.draw_networkx_edge_labels(g, pos)
plt.show()





