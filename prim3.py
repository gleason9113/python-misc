

nodes = {"A", "B", "C", "D", "E", "F"}
edges = {(("A", "D"), 1), (("A", "B"), 2), (("A", "E"), 4), (("A", "F"), 9), (("B", "F"), 3), (("B", "C"), 2)}
graph = dict()
for node in nodes:
    graph[node] = []
for edge in edges:
    print(edge[1])
    n1 = (edge[0])
    n2 = (edge[1])
    
    
print(graph)