import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations as combos
import random

#Generate a random, connected graph with randomly weighted edges
def rand_graph(node, seed):
    vertices = set([v for v in range(node)]) # Generate vertices
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
seed = 0.5
graph = rand_graph(node, seed)
graph2 = graph.copy()
test = list(graph.edges(2, data=True))
min = 11
min_edge = ()
for e in test:
    if e[2]['weight'] < min:
        min = e[2]['weight']
        min_edge = e
    #print(e[2]['weight'])
print(test)
print(min_edge)
graph2.remove_node(5)


min = 2
for(node1,node2,data) in graph.edges(data=True):
    if data['weight'] < min:
        min = data['weight']
    #print("Node1: " + str(node1) + " Node2: " + str(node2) + " Weight: " + str(data['weight']) + " Min: " + str(min))
    
        
    
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos)
# nx.draw_networkx_edge_labels(graph, pos)
plt.show()





